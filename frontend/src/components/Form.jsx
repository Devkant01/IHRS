import { useState } from "react";

export default function Form({ location, setLocation, onSubmit, loading }) {
    const [symptoms, setSymptoms] = useState("");
    const [gender, setGender] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({
            symptoms,
            location,          // already just district name
            doctor_gender: gender || undefined
        });
    };

    return (
        <form
            onSubmit={handleSubmit}
            className="max-w-lg mx-auto bg-white shadow-lg rounded-2xl p-6 space-y-5 border"
        >
            <div>
                <label className="block font-medium text-gray-700">Location (District)</label>
                <input
                    type="text"
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                    className="w-full border rounded-lg p-2 focus:ring-2 focus:ring-blue-500 outline-none"
                    placeholder="Detecting district..."
                />
            </div>
            <div>
                <label className="block font-medium text-gray-700">Symptoms / Disease</label>
                <input
                    type="text"
                    value={symptoms}
                    onChange={(e) => setSymptoms(e.target.value)}
                    className="w-full border rounded-lg p-2 focus:ring-2 focus:ring-blue-500 outline-none"
                    required
                />
            </div>
            <div>
                <label className="block font-medium text-gray-700">Doctor Gender (optional)</label>
                <select
                    value={gender}
                    onChange={(e) => setGender(e.target.value)}
                    className="w-full border rounded-lg p-2 focus:ring-2 focus:ring-blue-500 outline-none"
                >
                    <option value="">Any</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>
            </div>

            <button
                type="submit"
                className="w-full bg-blue-600 text-white py-2 rounded-lg font-medium hover:bg-blue-700 transition"
                disabled={loading}
            >
                {loading ? "Finding Doctors..." : "Get Recommendations"}
            </button>
        </form>
    );
}
