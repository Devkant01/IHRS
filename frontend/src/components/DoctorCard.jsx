import { MapPin, Stethoscope, User2 } from "lucide-react";

export default function DoctorCard({ doctor }) {
    return (
        <div className="bg-white rounded-2xl shadow-md border hover:shadow-xl transition p-5 flex flex-col gap-3">
            <div className="flex items-center justify-between">
                <h2 className="text-lg font-semibold text-blue-800">{doctor.name}</h2>
                <span className="text-sm px-3 py-1 rounded-full bg-blue-100 text-blue-700">
                    {doctor.gender}
                </span>
            </div>

            <div className="flex items-center gap-2 text-gray-700 text-sm">
                <Stethoscope size={16} className="text-green-600" />
                <span>Specialty: {doctor.specialties}</span>
            </div>

            <div className="flex items-center gap-2 text-gray-700 text-sm">
                <MapPin size={16} className="text-red-500" />
                <span>{doctor.location}</span>
            </div>

            <div className="flex items-center gap-2 text-gray-700 text-sm">
                <User2 size={16} className="text-purple-500" />
                <span>ID: {doctor.doctor_id}</span>
            </div>
        </div>
    );
}
