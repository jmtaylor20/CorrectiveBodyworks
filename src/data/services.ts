export type Service = {
  slug: string;
  title: string;
  summary: string;
  detail: string;
  icon: string; // key handed to <Icon />
};

export const services: Service[] = [
  {
    slug: 'orthopedic-physical-therapy',
    title: 'Orthopedic Physical Therapy',
    summary:
      'Individualized outpatient rehabilitation for injuries, post-operative recovery, and chronic orthopedic pain.',
    detail:
      'Every plan of care starts with a thorough evaluation of how you actually move. From there we build a progressive program of hands-on treatment and targeted exercise designed to restore strength, mobility, and confidence in the affected area — and to keep the problem from returning.',
    icon: 'activity',
  },
  {
    slug: 'manual-therapy',
    title: 'Manual Therapy',
    summary:
      'Skilled hands-on techniques that release restricted tissue and restore normal joint mechanics.',
    detail:
      'Joint mobilization, soft tissue work, and fascial techniques are used to address the restrictions that limit motion and drive pain. Manual therapy is rarely the whole answer on its own, so it is paired with corrective exercise that keeps the gains you make on the table.',
    icon: 'hands',
  },
  {
    slug: 'dry-needling',
    title: 'Integrative Dry Needling',
    summary:
      'A precise technique for calming overactive muscle tissue and relieving stubborn trigger points.',
    detail:
      'Integrative Dry Needling uses fine filament needles to treat neuromuscular pain and dysfunction at its source. It is especially effective for persistent muscular tightness and trigger points that have not responded to other approaches. Performed by a CIDN-certified clinician.',
    icon: 'needle',
  },
  {
    slug: 'sports-medicine',
    title: 'Sports Medicine',
    summary:
      'Injury care, return-to-play guidance, and performance work for athletes of every age.',
    detail:
      'From youth athletes through adult competitors, we treat the injury in front of us and then look upstream at the mechanics that produced it. The goal is a safe, well-paced return to sport with a lower risk of the same injury happening again.',
    icon: 'trophy',
  },
  {
    slug: 'corrective-exercise',
    title: 'Corrective Exercise',
    summary:
      'Targeted programming that resolves the muscular imbalances behind recurring pain.',
    detail:
      'Pain often shows up far from its actual cause. Corrective exercise addresses the postural and movement imbalances — the overworked muscles, the ones that stopped firing — so the body can distribute load the way it was designed to.',
    icon: 'balance',
  },
  {
    slug: 'running-orthotics',
    title: 'Running & Orthotic Intervention',
    summary:
      'Gait assessment and orthotic support for runners and anyone on their feet all day.',
    detail:
      'A specialty interest of the practice. We evaluate gait and foot mechanics, then use a combination of manual treatment, corrective exercise, and orthotic intervention where appropriate to keep you running comfortably and consistently.',
    icon: 'shoe',
  },
  {
    slug: 'industrial-athletes',
    title: 'Work & Industrial Injury',
    summary:
      'Rehabilitation for the "industrial athlete" — getting you back to work and back to life.',
    detail:
      'Physically demanding jobs place athletic loads on the body without any of the conditioning. We treat work-related injuries with the same rigor as sports injuries, focusing on the strength and mechanics your specific job actually requires.',
    icon: 'briefcase',
  },
  {
    slug: 'massage-therapy',
    title: 'Clinical Massage Therapy',
    summary:
      'Therapeutic massage and neuromuscular re-education delivered with clinical intent.',
    detail:
      'Myofascial release, deep tissue, sports massage, and neuromuscular re-education, applied as part of a treatment plan rather than as a standalone luxury. Useful for relaxing overstressed tissue and reactivating muscle that has gone quiet.',
    icon: 'wave',
  },
];

export const differentiators = [
  {
    title: 'We treat the cause, not just the symptom',
    body: 'Relief matters, and we deliver it. But the real work is finding the imbalance that produced the pain and correcting it, so you are not back in six months with the same complaint.',
  },
  {
    title: 'One clinician, start to finish',
    body: 'You see the same licensed clinician every visit — not a rotating cast of aides. Your treatment is delivered by the person who evaluated you and knows your history.',
  },
  {
    title: 'Advanced manual therapy training',
    body: 'CIDN, ART, PRRT, and Fascial Manipulation certifications mean a genuinely broad toolkit of hands-on techniques, matched to what your body actually needs.',
  },
  {
    title: 'More than 50 years of combined experience',
    body: 'Two seasoned clinicians who have seen an enormous range of cases across sports medicine, orthopedics, and rehabilitation.',
  },
];
