import { Info } from "lucide-react";

export default function Explanation({ explanations }) {
    // filter only doctor explanations
    const doctorMatches = explanations.filter((e) =>
        e.includes("matches your criteria")
    );

    if (doctorMatches.length === 0) return null;

    // extract doctor names
    const names = doctorMatches.map((e) =>
        e.replace("Doctor ", "").replace(" matches your criteria.", "")
    );

    let displayMsg = "";
    if (names.length === 1) {
        displayMsg = `Based on your criteria, ${names[0]} matches your profile.`;
    } else if (names.length === 2) {
        displayMsg = `Based on your criteria, ${names[0]} and ${names[1]} match your profile.`;
    } else {
        displayMsg = `Based on your criteria, ${names[0]}, ${names[1]} and +${names.length - 2
            } others match your profile.`;
    }

    return (
        <div className="flex items-start gap-2 bg-blue-50 border border-blue-200 p-3 rounded-xl">
            <Info className="text-blue-600 mt-0.5" size={18} />
            <p className="text-sm text-blue-800">{displayMsg}</p>
        </div>
    );
}
