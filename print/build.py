import pathlib, sys
SP = pathlib.Path(__file__).resolve().parent
FONTS = (SP / 'fonts.css').read_text()


def _logo(preferred, fallback):
    """Official full lockup when it is present, otherwise the two line mark.

    Drop the full 'CORRECTIVE BODYWORKS / REHABILITATION & WELLNESS' lockup in
    as print/logo-full.png (and a white knockout as print/logo-full-white.png)
    and every piece picks it up on the next build. Nothing else changes.
    """
    import base64
    src = SP / preferred
    if src.exists():
        return base64.b64encode(src.read_bytes()).decode(), True
    return (SP / fallback).read_text().strip(), False


LOGO, LOGO_IS_FULL = _logo('logo-full.png', 'logo.b64')

W = {
    'PAD_LOGO_W':   '1.32in' if LOGO_IS_FULL else '1.62in',
    'FLYER_LOGO_W': '2.15in' if LOGO_IS_FULL else '2.35in',
    'CARD_LOGO_W':  '1.26in' if LOGO_IS_FULL else '1.42in',
    'BACK_LOGO_W':  '1.62in' if LOGO_IS_FULL else '1.85in',
}

BASE = """
%(fonts)s
:root{
  --navy:#011B3A; --slate:#4C647A; --mist:#CED4DA;
  --rule:#B9C2CC; --ink:#16202E; --muted:#5A6878;
  --display:'Barlow Condensed','Arial Narrow',sans-serif;
  --body:'Source Sans 3',Helvetica,Arial,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{background:#fff;color:var(--ink);font-family:var(--body);
  -webkit-print-color-adjust:exact;print-color-adjust:exact;}
.logo{display:block;}
.eyebrow{font-size:6.2pt;font-weight:700;letter-spacing:.16em;
  text-transform:uppercase;color:var(--slate);}
"""

def write(name, page_css, body):
    for k, v in W.items():
        page_css = page_css.replace(k, v)
    html = ("<!doctype html><meta charset='utf-8'><style>"
            + BASE % {'fonts': FONTS} + page_css + "</style>" + body)
    (SP / name).write_text(html)
    print('wrote', name, f"{(SP/name).stat().st_size/1024:.0f}KB")

# ------------------------------------------------------------------ pad
pad_css = """
@page{size:5.5in 8.5in;margin:0;}
body{width:5.5in;height:8.5in;padding:.32in .36in .24in;display:flex;flex-direction:column;}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:.18in;
  border-bottom:2.5pt solid var(--navy);padding-bottom:.1in;}
.head img{width:PAD_LOGO_W;}
.head .npi{text-align:right;font-size:6.4pt;line-height:1.5;color:var(--muted);}
.head .npi b{display:block;font-size:6.2pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--slate);}
h1{font-family:var(--display);font-size:17pt;font-weight:600;letter-spacing:.03em;
  text-transform:uppercase;color:var(--navy);margin:.1in 0 .02in;line-height:1;}
.sub{font-size:7pt;color:var(--muted);margin-bottom:.09in;}
.grp{margin-bottom:.085in;}
.grp>.eyebrow{display:block;margin-bottom:.045in;}
.row{display:flex;gap:.15in;}
.f{flex:1;min-width:0;}
.f label{display:block;font-size:6.3pt;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin-bottom:.04in;}
.line{border-bottom:.75pt solid var(--rule);height:.15in;}
.line.tall{height:.25in;}
.box{border:.75pt solid var(--rule);height:.42in;}
.checks{display:flex;flex-wrap:wrap;gap:.05in .16in;font-size:7.4pt;color:var(--ink);}
.ck{display:flex;align-items:center;gap:.045in;}
.ck i{width:.105in;height:.105in;border:.9pt solid var(--navy);display:inline-block;}
.orders{background:#F4F6F8;border-left:2.5pt solid var(--slate);
  padding:.08in .1in;margin-bottom:.085in;}
.orow{display:flex;align-items:center;flex-wrap:wrap;gap:.04in .13in;
  font-size:7.4pt;margin-top:.06in;}
.olab{font-size:6.3pt;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);width:1.2in;flex:none;}
.ounit{font-size:6.9pt;color:var(--muted);}
.dateline{border-bottom:.75pt solid var(--rule);flex:1;min-width:1.2in;height:.15in;}
.clin{margin-top:auto;background:#F4F6F8;padding:.07in .1in;margin-bottom:.085in;}
.clin .who{display:flex;gap:.2in;margin-top:.05in;}
.clin .who div{font-size:7.2pt;line-height:1.35;}
.clin .who b{color:var(--navy);}
.clin .who span{display:block;font-size:6.4pt;color:var(--muted);
  letter-spacing:.06em;text-transform:uppercase;}
.clin .tech{font-size:6.5pt;color:var(--muted);margin-top:.06in;line-height:1.4;}
.clin .tech b{font-size:6.1pt;letter-spacing:.11em;text-transform:uppercase;
  color:var(--slate);margin-right:.04in;}
.sig{border-top:.75pt solid var(--rule);padding-top:.08in;}
.foot{margin-top:.1in;border-top:2.5pt solid var(--navy);padding-top:.07in;
  display:flex;justify-content:space-between;align-items:flex-end;gap:.12in;}
.foot .addr{font-size:6.6pt;line-height:1.45;color:var(--muted);}
.foot .addr b{color:var(--navy);}
.foot .send{text-align:right;font-size:6.6pt;line-height:1.45;color:var(--muted);}
"""

pad_body = """
<div class="head">
  <img class="logo" src="data:image/png;base64,%(logo)s" alt="Corrective Bodyworks Rehabilitation and Wellness">
  <div class="npi"><b>Group NPI</b>1356299622<br>Notasulga, Alabama</div>
</div>

<h1>Physical Therapy Referral</h1>
<p class="sub">Evaluation and treatment by a licensed physical therapist.</p>

<div class="grp">
  <span class="eyebrow">Patient</span>
  <div class="row">
    <div class="f" style="flex:2"><label>Name</label><div class="line"></div></div>
    <div class="f"><label>Date of birth</label><div class="line"></div></div>
  </div>
  <div class="row" style="margin-top:.075in">
    <div class="f"><label>Phone</label><div class="line"></div></div>
    <div class="f"><label>Date of referral</label><div class="line"></div></div>
  </div>
</div>

<div class="grp">
  <span class="eyebrow">Diagnosis</span>
  <div class="row">
    <div class="f" style="flex:2.2"><label>Diagnosis</label><div class="line"></div></div>
    <div class="f"><label>ICD-10</label><div class="line"></div></div>
  </div>
  <div class="row" style="margin-top:.075in">
    <div class="f"><label>Date of onset or surgery</label><div class="line"></div></div>
    <div class="f">
      <label>Side</label>
      <div class="checks" style="padding-top:.03in">
        <span class="ck"><i></i>Left</span><span class="ck"><i></i>Right</span>
        <span class="ck"><i></i>Bilateral</span><span class="ck"><i></i>N/A</span>
      </div>
    </div>
  </div>
</div>

<div class="orders">
  <span class="eyebrow">Orders</span>
  <div class="checks" style="margin-top:.055in">
    <span class="ck"><i></i><b>Evaluate and treat</b></span>
    <span class="ck"><i></i>Post-op protocol attached</span>
  </div>
  <div class="orow">
    <span class="olab">Frequency</span>
    <span class="ck"><i></i>1x</span><span class="ck"><i></i>2x</span>
    <span class="ck"><i></i>3x</span><span class="ck"><i></i>4x</span>
    <span class="ounit">per week</span>
  </div>
  <div class="orow">
    <span class="olab">Duration</span>
    <span class="ck"><i></i>2</span><span class="ck"><i></i>4</span>
    <span class="ck"><i></i>6</span><span class="ck"><i></i>8</span>
    <span class="ck"><i></i>12</span>
    <span class="ounit">weeks</span>
  </div>
  <div class="orow">
    <span class="olab">Return to physician</span>
    <span class="dateline"></span>
  </div>
</div>

<div class="grp">
  <span class="eyebrow">Precautions and weight bearing</span>
  <div class="checks" style="margin:.055in 0 .06in">
    <span class="ck"><i></i>None</span><span class="ck"><i></i>WBAT</span>
    <span class="ck"><i></i>PWB</span><span class="ck"><i></i>NWB</span>
    <span class="ck"><i></i>TTWB</span><span class="ck"><i></i>Per protocol</span>
  </div>
  <div class="row">
    <div class="f"><label>Other restrictions</label><div class="line"></div></div>
  </div>
</div>

<div class="clin">
  <span class="eyebrow">Treating clinicians</span>
  <div class="who">
    <div><b>Cameron Elliott, PT, MPT</b><span>Physical Therapist</span></div>
    <div><b>Jeff Cotten, PTA, ATC, LMT, CIDN</b><span>Physical Therapist Assistant</span></div>
  </div>
  <div class="tech"><b>Services</b> Post-operative rehabilitation, outpatient
    orthopedics, sports injury, work injury and return to work, balance and fall
    prevention, orthopedic manual therapy, dry needling, orthotic assessment.</div>
</div>

<div class="sig">
  <span class="eyebrow" style="display:block;margin-bottom:.06in">Referring provider</span>
  <div class="row">
    <div class="f"><label>Name</label><div class="line"></div></div>
  </div>
  <div class="row" style="margin-top:.075in">
    <div class="f" style="flex:2"><label>Signature</label><div class="line tall"></div></div>
    <div class="f"><label>Date</label><div class="line tall"></div></div>
  </div>
</div>

<div class="foot">
  <div class="addr">
    <b>Corrective Bodyworks Rehabilitation &amp; Wellness</b><br>
    17257 Highway 49 South, Notasulga, AL 36866<br>
    Phone (334) 319-1684 &nbsp;|&nbsp; Fax (334) 625-6578
  </div>
  <div class="send">
    <b style="color:var(--navy);font-size:7.6pt">Fax to (334) 625-6578</b>
    or send this form with your patient.<br>
    We contact every referral within one business day.
  </div>
</div>
""" % {'logo': LOGO}

write('referral-pad.html', pad_css, pad_body)

# --------------------------------------------------------------- flyer
flyer_css = """
@page{size:8.5in 11in;margin:0;}
body{width:8.5in;height:11in;padding:.42in .5in .34in;display:flex;flex-direction:column;}
.top{display:flex;justify-content:space-between;align-items:flex-start;
  border-bottom:3pt solid var(--navy);padding-bottom:.13in;}
.top img{width:FLYER_LOGO_W;}
.top .meta{text-align:right;font-size:7.4pt;line-height:1.55;color:var(--muted);}
.top .meta b{display:block;font-size:6.6pt;letter-spacing:.15em;
  text-transform:uppercase;color:var(--slate);margin-bottom:.02in;}
h1{font-family:var(--display);font-size:38pt;font-weight:600;line-height:.95;
  letter-spacing:.015em;text-transform:uppercase;color:var(--navy);margin:.18in 0 .09in;}
h1 em{font-style:normal;color:var(--slate);}
.lede{font-size:11pt;line-height:1.5;color:var(--muted);max-width:6.1in;}
.split{display:flex;gap:.42in;margin-top:.24in;}
.col{flex:1;}
h2{font-family:var(--display);font-size:13.5pt;font-weight:600;letter-spacing:.05em;
  text-transform:uppercase;color:var(--navy);margin-bottom:.09in;
  padding-bottom:.05in;border-bottom:1pt solid var(--mist);}
ul{list-style:none;}
li{font-size:9.2pt;line-height:1.45;color:var(--ink);padding-left:.16in;
  position:relative;margin-bottom:.055in;}
li:before{content:'';position:absolute;left:0;top:.055in;width:.055in;height:.055in;
  background:var(--slate);}
.why{margin-top:.24in;background:var(--navy);color:#fff;padding:.22in .26in;}
.why h2{color:#fff;border-bottom-color:rgba(255,255,255,.28);}
.why .three{display:flex;gap:.3in;margin-top:.12in;}
.why .three div{flex:1;}
.why .three b{display:block;font-family:var(--display);font-size:12pt;
  letter-spacing:.03em;color:#fff;margin-bottom:.04in;}
.why .three p{font-size:8.6pt;line-height:1.45;color:var(--mist);}
.people{display:flex;gap:.32in;margin-top:.22in;}
.people div{flex:1;border-left:2.5pt solid var(--slate);padding-left:.14in;}
.people b{font-size:10.2pt;color:var(--navy);display:block;}
.people span{font-size:6.9pt;letter-spacing:.13em;text-transform:uppercase;
  color:var(--slate);display:block;margin:.02in 0 .05in;}
.people p{font-size:8.6pt;line-height:1.45;color:var(--muted);}
.strip{display:flex;gap:0;margin-top:.22in;border:1pt solid var(--mist);}
.strip div{flex:1;padding:.13in .15in;border-right:1pt solid var(--mist);}
.strip div:last-child{border-right:0;}
.strip b{display:block;font-size:6.6pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--slate);margin-bottom:.05in;}
.strip p{font-size:8.4pt;line-height:1.42;color:var(--ink);}
.foot{margin-top:auto;border-top:3pt solid var(--navy);padding-top:.13in;
  display:flex;justify-content:space-between;align-items:flex-end;gap:.3in;}
.foot .a{font-size:8.6pt;line-height:1.5;color:var(--muted);}
.foot .a b{font-size:10pt;color:var(--navy);display:block;margin-bottom:.03in;}
.foot .cta{text-align:right;font-size:8.6pt;line-height:1.5;color:var(--muted);}
.foot .cta b{display:block;font-family:var(--display);font-size:15pt;
  letter-spacing:.03em;text-transform:uppercase;color:var(--navy);}
"""

flyer_body = """
<div class="top">
  <img class="logo" src="data:image/png;base64,%(logo)s" alt="Corrective Bodyworks Rehabilitation and Wellness">
  <div class="meta"><b>Now accepting referrals</b>
    17257 Highway 49 South<br>Notasulga, Alabama 36866<br>Group NPI 1356299622</div>
</div>

<h1>Outpatient orthopedic PT,<br><em>one patient at a time.</em></h1>
<p class="lede">
  A new outpatient clinic in Notasulga built around unhurried, hands-on care.
  Four treatment rooms and a deliberately manageable caseload, so your patient
  is seen promptly and treated by the same clinician at every visit.
</p>

<div class="split">
  <div class="col">
    <h2>What we treat</h2>
    <ul>
      <li>Outpatient orthopedic conditions</li>
      <li>Post-surgical rehabilitation</li>
      <li>Sports injuries, youth through adult</li>
      <li>Work injury and return to work</li>
      <li>Balance and fall prevention</li>
      <li>Running mechanics and orthotic intervention</li>
      <li>Chronic pain and movement dysfunction</li>
    </ul>
  </div>
  <div class="col">
    <h2>Advanced techniques</h2>
    <ul>
      <li>Integrative dry needling (CIDN certified)</li>
      <li>Active Release Techniques (ART)</li>
      <li>Primal Reflex Release Techniques (PRRT)</li>
      <li>Fascial Manipulation</li>
      <li>Manual and soft tissue therapy</li>
      <li>Corrective exercise programming</li>
      <li>Orthotic assessment</li>
    </ul>
  </div>
</div>

<div class="why">
  <h2>Why refer here</h2>
  <div class="three">
    <div><b>Prompt access</b><p>We contact every referral within one business day
      and work to see new patients quickly, so your patient does not wait weeks
      to start.</p></div>
    <div><b>Real hands-on time</b><p>Unhurried appointments delivered one on one
      by a licensed clinician, with time to assess properly and adjust the plan
      as your patient progresses.</p></div>
    <div><b>You stay informed</b><p>You receive the evaluation, the plan of care,
      and progress updates. Your patient comes back to you, not to someone else.</p></div>
  </div>
</div>

<div class="people">
  <div>
    <b>Cameron Elliott, PT, MPT</b><span>Physical Therapist</span>
    <p>More than 25 years treating patients of every age and activity level.
      M.P.T., University of South Alabama. B.S. Microbiology, Auburn University.</p>
  </div>
  <div>
    <b>Jeff Cotten, PTA, ATC, LMT, CIDN</b><span>Physical Therapist Assistant</span>
    <p>Nearly 30 years across outpatient orthopedics, manual therapy and sports
      medicine. Certified athletic trainer, licensed massage therapist, CIDN, ART.</p>
  </div>
</div>

<div class="strip">
  <div><b>Insurance</b><p>All major insurances accepted, including workers
    compensation. Please call to confirm your patient's coverage.</p></div>
  <div><b>Hours</b><p>Flexible hours to accommodate busy schedules, including
    early morning and evening appointments.</p></div>
  <div><b>How to refer</b><p>Fax to (334) 625-6578, call the clinic, or send your
    patient with a referral slip from our pad.</p></div>
</div>

<div class="foot">
  <div class="a"><b>Corrective Bodyworks Rehabilitation &amp; Wellness</b>
    17257 Highway 49 South, Notasulga, AL 36866<br>
    jeff@correctiverehab.com</div>
  <div class="cta">Referrals and questions<br><b>(334) 319-1684</b>
    Fax (334) 625-6578</div>
</div>
""" % {'logo': LOGO}

write('physician-flyer.html', flyer_css, flyer_body)

# --------------------------------------------------------------- cards
LOGO_W, _ = _logo('logo-full-white.png', 'logo-white.b64')

# 3.5 x 2 in trim, plus .125 in bleed on every edge = 3.75 x 2.25 in.
# Content sits .25 in inside the bleed edge, which is .125 in inside the trim.
card_css = """
@page{size:3.75in 2.25in;margin:0;}
body{width:3.75in;}
.card{width:3.75in;height:2.25in;padding:.28in .28in .28in .3in;position:relative;
  overflow:hidden;display:flex;flex-direction:column;page-break-after:always;}
.card:last-child{page-break-after:auto;}
.face{background:#fff;}
.face:before{content:'';position:absolute;left:0;top:0;bottom:0;width:.2in;
  background:var(--navy);}
.face img{width:CARD_LOGO_W;}
.face .who{margin-top:auto;}
.face .nm{font-family:var(--display);font-size:14pt;font-weight:600;
  letter-spacing:.02em;color:var(--navy);line-height:1;}
.face .cr{font-size:6.1pt;font-weight:700;letter-spacing:.11em;
  text-transform:uppercase;color:var(--slate);margin:.035in 0 .015in;}
.face .ti{font-size:7.2pt;color:var(--muted);}
.face .contact{display:flex;justify-content:space-between;align-items:flex-end;
  gap:.12in;margin-top:.11in;padding-top:.075in;border-top:.75pt solid var(--mist);
  font-size:6.5pt;line-height:1.5;color:var(--muted);}
.face .contact b{display:block;color:var(--navy);font-size:7.4pt;font-weight:700;}
.face .contact .r{text-align:right;}
.back{background:var(--navy);align-items:center;justify-content:center;text-align:center;}
.back img{width:BACK_LOGO_W;margin-bottom:.11in;}
.back .tag{font-size:6.4pt;font-weight:700;letter-spacing:.15em;
  text-transform:uppercase;color:var(--mist);line-height:1.7;}
.back .det{margin-top:.09in;font-size:6.9pt;line-height:1.55;color:#fff;}
"""

def card(slug, name, creds, title, email):
    body = """
<div class="card face">
  <img src="data:image/png;base64,%(logo)s" alt="">
  <div class="who">
    <div class="nm">%(name)s</div>
    <div class="cr">%(creds)s</div>
    <div class="ti">%(title)s</div>
    <div class="contact">
      <div><b>(334) 319-1684</b>Fax (334) 625-6578</div>
      <div class="r">%(email)s<br>correctiverehab.com<br>17257 Highway 49 S, Notasulga, AL 36866</div>
    </div>
  </div>
</div>

<div class="card back">
  <img src="data:image/png;base64,%(logow)s" alt="Corrective Bodyworks Rehabilitation and Wellness">
  <div class="tag">Outpatient Orthopedics &nbsp;&middot;&nbsp; Manual Therapy<br>
    Sports Medicine &nbsp;&middot;&nbsp; Dry Needling</div>
  <div class="det">correctiverehab.com<br>Notasulga, Alabama &nbsp;&middot;&nbsp; (334) 319-1684</div>
</div>
""" % {'logo': LOGO, 'logow': LOGO_W, 'name': name, 'creds': creds,
       'title': title, 'email': email}
    write('card-%s.html' % slug, card_css, body)

card('jeff', 'Jeff Cotten', 'PTA, ATC, LMT, CIDN', 'Owner and Clinician',
     'jeff@correctiverehab.com')
card('cameron', 'Cameron Elliott', 'PT, MPT', 'Physical Therapist',
     'cameron@correctiverehab.com')
