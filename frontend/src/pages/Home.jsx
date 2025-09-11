import { useEffect, useState } from "react";
import Form from "../components/Form";
import DoctorCard from "../components/DoctorCard";
import Explanation from "../components/Explanation";
import { getRecommendations } from "../services/api";

export default function Home() {
    const [location, setLocation] = useState("");
    const [loading, setLoading] = useState(false);
    const [explanations, setExplanations] = useState([]);
    const [recommendations, setRecommendations] = useState([]);

    // Auto-detect location → only district name
    useEffect(() => {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(
                async (pos) => {
                    const { latitude, longitude } = pos.coords;
                    try {
                        const res = await fetch(
                            `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}`
                        );
                        const data = await res.json();

                        // Extract district (suburb/town/city/county)
                        const district =
                            data.address?.county ||
                            data.address?.city ||
                            data.address?.town ||
                            data.address?.state_district ||
                            "";

                        setLocation(district);
                    } catch {
                        setLocation("");
                    }
                },
                () => setLocation("")
            );
        }
    }, []);

    const handleSubmit = async (formData) => {
        setLoading(true);
        setExplanations([]);
        setRecommendations([]);

        try {
            const data = await getRecommendations(formData);

            // Filter out unwanted explanations
            const cleanExplanations = (data.explanations || []).filter(
                (msg) => !msg.includes("Collaborative filtering")
            );

            setExplanations(cleanExplanations);
            setRecommendations(data.recommendations || []);
        } catch (err) {
            console.error("Error:", err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-6">
            <h1 className="text-3xl font-bold text-center mb-8 text-blue-900">
                🩺 Healthcare Recommendation
            </h1>

            <Form
                location={location}
                setLocation={setLocation}
                onSubmit={handleSubmit}
                loading={loading}
            />

            <div className="max-w-2xl mx-auto mt-8 space-y-5">
                <Explanation explanations={explanations} />

                {recommendations.length === 0 && !loading && (
                    <p className="text-center text-gray-600 italic">
                        No doctors found for your criteria.
                    </p>
                )}

                <div className="grid sm:grid-cols-2 gap-5">
                    {recommendations.map((doc) => (
                        <DoctorCard key={doc.doctor_id} doctor={doc} />
                    ))}
                </div>
            </div>
        </div>
    );
}
