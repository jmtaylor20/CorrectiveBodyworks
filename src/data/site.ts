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

  // Google Maps deep link, works without an API key.
  mapsUrl:
    'https://www.google.com/maps/search/?api=1&query=17257+Highway+49+S+Notasulga+AL+36866',
  mapsEmbedUrl:
    'https://www.google.com/maps?q=17257+Highway+49+S+Notasulga+AL+36866&output=embed',

  hours: [
    { day: 'Monday to Thursday', time: '8:00 AM to 5:00 PM' },
    { day: 'Friday', time: '8:00 AM to 12:00 PM' },
    { day: 'Saturday to Sunday', time: 'Closed' },
  ],

  // PT Everywhere.
  //
  // `url` is the public self-booking link patients use to request an
  // appointment. `portalUrl` is the existing-patient login. Both are issued
  // from the PT Everywhere account; ask Client Care for the practice's
  // booking and portal links.
  //
  // Leave a value empty and the site falls back gracefully: booking buttons
  // point at /contact/, and the portal link is hidden entirely. Paste a URL
  // in and every call to action across the site switches over. No other file
  // needs to change.
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

/**
 * Where the primary call to action points. Uses the PT Everywhere booking
 * link when one is configured, otherwise the contact form.
 */
export const bookingHref = (): string => site.booking.url || '/contact/';

/** True when the booking link leaves our domain and needs target/rel. */
export const bookingIsExternal = (): boolean => /^https?:/i.test(site.booking.url);

/** The existing-patient portal link, or null when none is configured. */
export const portalHref = (): string | null => site.booking.portalUrl || null;
