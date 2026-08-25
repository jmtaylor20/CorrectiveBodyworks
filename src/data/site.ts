// ---------------------------------------------------------------------------
// Single source of truth for business details. Every page reads from here, so
// changing a phone number or an address is a one-line edit.
// ---------------------------------------------------------------------------

export const site = {
  name: 'Corrective Bodyworks',
  legalName: 'Corrective Bodyworks, LLC',
  tagline: 'Rehabilitation & Wellness',
  description:
    'Outpatient orthopedic physical therapy, manual therapy, and sports medicine in Notasulga, Alabama. Personalized, hands-on care that relieves pain, restores function, and corrects the imbalances behind it.',

  phone: '(334) 319-1684',
  phoneHref: 'tel:+13343191684',
  email: 'info@correctivebodyworks.net',

  address: {
    street: '17257 Highway 49 S',
    city: 'Notasulga',
    state: 'AL',
    zip: '36866',
    get full() {
      return `${this.street}, ${this.city}, ${this.state} ${this.zip}`;
    },
  },

  // Google Maps deep link — works without an API key.
  mapsUrl:
    'https://www.google.com/maps/search/?api=1&query=17257+Highway+49+S+Notasulga+AL+36866',
  mapsEmbedUrl:
    'https://www.google.com/maps?q=17257+Highway+49+S+Notasulga+AL+36866&output=embed',

  hours: [
    { day: 'Monday – Thursday', time: '8:00 AM – 5:00 PM' },
    { day: 'Friday', time: '8:00 AM – 12:00 PM' },
    { day: 'Saturday – Sunday', time: 'Closed' },
  ],

  // TODO: replace with the live PT Everywhere booking/portal URLs once issued.
  booking: {
    url: '',
    portalUrl: '',
    label: 'Request an Appointment',
  },

  social: {
    facebook: '',
    instagram: '',
  },
} as const;

export const nav = [
  { label: 'About', href: '/about/' },
  { label: 'Our Team', href: '/team/' },
  { label: 'Services', href: '/services/' },
  { label: 'Contact', href: '/contact/' },
] as const;
