export type TeamMember = {
  slug: string;
  name: string;
  credentials: string;
  role: string;
  photo: string | null;
  lede: string;
  bio: string[];
  certifications: string[];
  focus: string[];
  education?: string[];
  personal: string;
};

export const team: TeamMember[] = [
  {
    slug: 'jeff-cotten',
    name: 'Jeff Cotten',
    credentials: 'PTA, ATC, LMT, CIDN',
    role: 'Owner & Clinician',
    // TODO: add Jeff's headshot to /public/team/jeff-cotten.jpg
    photo: null,
    lede:
      'Nearly 30 years of hands-on experience, focused on finding and correcting the imbalance behind the pain — not just treating the symptom.',
    bio: [
      'Jeff Cotten is a Physical Therapist Assistant, Certified Athletic Trainer, Corrective Exercise Specialist, and Licensed Massage Therapist with nearly 30 years of experience across a wide range of clinical settings. His practice centers on outpatient orthopedic physical therapy, manual therapy, and sports medicine.',
      'Jeff has invested heavily in advanced manual therapy training, holding certifications in Integrative Dry Needling, Active Release Techniques, Primal Reflex Release Techniques, and Fascial Manipulation. He uses those tools to bring real relief and restore function — but his larger goal is always to correct the underlying musculoskeletal imbalances that caused the problem, so pain and dysfunction do not come back.',
      'He works with patients of every kind: adult and youth athletes, people rehabilitating an injury, and the "industrial athletes" whose work puts hard demands on their bodies. Jeff has a particular interest in runners and in orthotic intervention, and he takes real satisfaction in helping people get back to work and back to enjoying life.',
    ],
    certifications: [
      'CIDN — Certified Integrative Dry Needling',
      'ART — Active Release Techniques',
      'PRRT — Primal Reflex Release Techniques',
      'Fascial Manipulation',
      'Certified Athletic Trainer (ATC)',
      'Corrective Exercise Specialist',
      'Licensed Massage Therapist',
    ],
    focus: [
      'Outpatient orthopedic physical therapy',
      'Manual & soft tissue therapy',
      'Sports medicine',
      'Runners & orthotic intervention',
      'Work & industrial injury recovery',
      'Postural and movement correction',
    ],
    personal:
      'Jeff is married with three children. Outside the clinic he is active in his church family and spends as much time outdoors as he can — hunting, fishing, and camping.',
  },
  {
    slug: 'cameron-elliott',
    name: 'Cameron Elliott',
    credentials: 'PT, MPT',
    role: 'Physical Therapist',
    photo: '/team/cameron-elliott.jpg',
    lede:
      'More than 25 years of helping patients restore mobility, reduce pain, and get back to the activities they love most.',
    bio: [
      'Cameron Elliott is a licensed physical therapist with more than 25 years of experience helping patients restore mobility, reduce pain, and return to the activities they enjoy most.',
      'Across a career spanning more than two decades, Cameron has treated patients of every age and activity level, delivering personalized, evidence-based care built around lasting results rather than short-term relief. She is committed to compassionate, patient-centered treatment, and she works with each person to reach their own specific rehabilitation and wellness goals.',
    ],
    certifications: ['Licensed Physical Therapist'],
    focus: [
      'Orthopedic rehabilitation',
      'Mobility & pain reduction',
      'Patients of all ages and activity levels',
      'Evidence-based, individualized care',
      'Return to sport and daily activity',
    ],
    education: [
      'M.P.T., Physical Therapy — University of South Alabama, 2001',
      'B.S., Microbiology — Auburn University, 1998',
    ],
    personal:
      'In her free time, Cameron enjoys being with her husband Ben and their son Everett. They are avid sports fans, and you can usually find them at a nearby ball field.',
  },
];
