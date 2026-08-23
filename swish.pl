% Hospital Doctor Recommendation System

patient(aarav).
patient(neha).
patient(rohan).
patient(kavya).
patient(aditya).

symptom(aarav,fever).
symptom(aarav,cough).
symptom(neha,headache).
symptom(neha,dizziness).
symptom(rohan,chest_pain).
symptom(rohan,breathing_problem).
symptom(kavya,skin_rash).
symptom(aditya,joint_pain).

doctor(mehta,general_medicine).
doctor(shah,neurology).
doctor(patil,cardiology).
doctor(joshi,dermatology).
doctor(rao,orthopedics).

treats(general_medicine,fever).
treats(general_medicine,cough).

treats(neurology,headache).
treats(neurology,dizziness).

treats(cardiology,chest_pain).
treats(cardiology,breathing_problem).

treats(dermatology,skin_rash).
treats(orthopedics,joint_pain).

available(mehta,monday).
available(mehta,wednesday).
available(shah,tuesday).
available(shah,thursday).
available(patil,monday).
available(patil,friday).
available(joshi,wednesday).
available(rao,tuesday).
available(rao,saturday).

department(general_medicine,ground_floor).
department(neurology,first_floor).
department(cardiology,second_floor).
department(dermatology,first_floor).
department(orthopedics,second_floor).

specialization(Patient,Specialization) :-
    symptom(Patient,Symptom),
    treats(Specialization,Symptom).

suitable_doctor(Patient,Doctor) :-
    specialization(Patient,Specialization),
    doctor(Doctor,Specialization).

recommend(Patient,Doctor) :-
    suitable_doctor(Patient,Doctor),
    available(Doctor,_).

recommend_appointment(Patient,Doctor,Day) :-
    suitable_doctor(Patient,Doctor),
    available(Doctor,Day).

doctor_location(Doctor,Floor) :-
    doctor(Doctor,Specialization),
    department(Specialization,Floor).

available_doctor(Day,Doctor) :-
    available(Doctor,Day).

patient_with_symptom(Symptom,Patient) :-
    symptom(Patient,Symptom).