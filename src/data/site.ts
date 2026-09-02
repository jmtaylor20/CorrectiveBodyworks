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
  // Each practice gets its own public PT Everywhere pages, following the
  // pattern used by other PT Everywhere clinics:
  //
  //   portal:   https://pteverywhere.com/PtE/s/<slug>
  //   register: https://pteverywhere.com/PtE/s/<slug>/register
  //
  // Ask PT Everywhere Client Care for this practice's exact slug. Do not
  // guess it: the pages are client-rendered, so a wrong slug fails silently
  // rather than 404ing, and could send patients to another clinic.
  //
  // Set `clinicUrl` and `registerUrl` below and the portal page and header
  // link switch to them automatically. While they are empty the site falls
  // back to the generic PT Everywhere login, which still works.
  portal: {
    clinicUrl: '',
    registerUrl: '',
    login: 'https://app.pteverywhere.com/',
    help: 'https://help.pteverywhere.com/kb',
    ios: 'https://apps.apple.com/us/app/pteverywhere/id1097797473',
    android:
      'https://play.google.com/store/apps/details?id=com.somotsoft.pteverywhere',
  },

  booking: {
    url: '',
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
 * Where the primary call to action points, in order of preference:
 * a self-booking link, then new-patient registration, then the contact form.
 * A new patient who cannot self-book should still land somewhere useful.
 */
export const bookingHref = (): string =>
  site.booking.url || site.portal.registerUrl || '/contact/';

/** True when the booking link leaves our domain and needs target/rel. */
export const bookingIsExternal = (): boolean => /^https?:/i.test(bookingHref());

/** Where patients sign in: the practice's own PT Everywhere page when it is
 *  configured, otherwise the generic PT Everywhere login. */
export const portalLoginHref = (): string =>
  site.portal.clinicUrl || site.portal.login;

/** The practice's new-patient registration page, or null when not set. */
export const portalRegisterHref = (): string | null =>
  site.portal.registerUrl || null;
