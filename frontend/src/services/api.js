export async function getRecommendations({ symptoms, location, doctor_gender }) {
    const res = await fetch("http://localhost:5000/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symptoms, location, doctor_gender }),
    });

    if (!res.ok) {
        throw new Error("Failed to fetch recommendations");
    }

    return res.json();
}
