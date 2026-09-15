// ---------------------------------------------------------------------------
// Single source of truth for business details. Every page reads from here, so
// changing a phone number or an address is a one-line edit.
// ---------------------------------------------------------------------------

export const site = {
  name: 'Corrective Bodyworks',
  legalName: 'Corrective Bodyworks, LLC',
  tagline: 'Rehabilitation & Wellness',
  description:
    'Outpatient orthopedic physical therapy, manual therapy and sports medicine in Notasulga, Alabama. Hands-on care that treats the cause, not just the symptom.',

  phone: '(334) 319-1684',
  phoneHref: 'tel:+13343191684',
  fax: '(334) 625-6578',
  email: 'jeff@correctiverehab.com',

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
  mapsDirections:
    'https://www.google.com/maps/dir/?api=1&destination=17257+Highway+49+S+Notasulga+AL+36866',
  appleMaps:
    'https://maps.apple.com/?daddr=17257+Highway+49+S,+Notasulga,+AL+36866',

  hours: [
    { day: 'Monday and Wednesday', time: '7:30 AM to 4:30 PM' },
    { day: 'Tuesday and Thursday', time: '9:00 AM to 6:00 PM' },
    { day: 'Friday', time: '7:30 AM to 12:00 PM' },
    { day: 'Saturday and Sunday', time: 'Closed' },
  ],

  // PT Everywhere.
  //
  // Live links issued by PT Everywhere Client Care for this practice. Note
  // the two paths are not symmetrical: registration sits under /s/ and
  // online booking does not. Copy them exactly, do not tidy them up.
  //
  // Every page is client rendered, so a wrong id returns a normal looking
  // empty shell rather than a 404. Click both after any change.
  portal: {
    // Public self-scheduling. Drives every "Request an Appointment" button.
    booking:
      'https://app.pteverywhere.com/69d3ad9de10addc51c61ac84/bookingonline',
    // New patient self registration.
    registerUrl:
      'https://app.pteverywhere.com/s/69d3ad9de10addc51c61ac84/register',
    // Existing patient sign in. PT Everywhere has not issued a practice
    // specific login page, so this is the shared one, which is correct.
    login: 'https://app.pteverywhere.com/',
    help: 'https://help.pteverywhere.com/kb',
    ios: 'https://apps.apple.com/us/app/pteverywhere/id1097797473',
    android:
      'https://play.google.com/store/apps/details?id=com.somotsoft.pteverywhere',
  },

  booking: {
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
  site.portal.booking || site.portal.registerUrl || '/contact/';

/** True when the booking link leaves our domain and needs target/rel. */
export const bookingIsExternal = (): boolean => /^https?:/i.test(bookingHref());

/** Where patients sign in: the practice's own PT Everywhere page when it is
 *  configured, otherwise the generic PT Everywhere login. */
export const portalLoginHref = (): string => site.portal.login;

/** The practice's new-patient registration page, or null when not set. */
export const portalRegisterHref = (): string | null =>
  site.portal.registerUrl || null;
