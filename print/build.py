import pathlib, sys
SP = pathlib.Path('/tmp/claude-0/-home-user-CorrectiveBodyworks/3751cb04-a410-5b87-a4c3-8d78e0f7a487/scratchpad/print')
FONTS = (SP / 'fonts.css').read_text()
LOGO = (SP / 'logo.b64').read_text().strip()

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
.head img{width:1.62in;}
.head .npi{text-align:right;font-size:6.4pt;line-height:1.5;color:var(--muted);}
.head .npi b{display:block;font-size:6.2pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--slate);}
h1{font-family:var(--display);font-size:17pt;font-weight:600;letter-spacing:.03em;
  text-transform:uppercase;color:var(--navy);margin:.13in 0 .02in;line-height:1;}
.sub{font-size:7pt;color:var(--muted);margin-bottom:.11in;}
.grp{margin-bottom:.115in;}
.grp>.eyebrow{display:block;margin-bottom:.055in;}
.row{display:flex;gap:.15in;}
.f{flex:1;min-width:0;}
.f label{display:block;font-size:6.3pt;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);margin-bottom:.055in;}
.line{border-bottom:.75pt solid var(--rule);height:.19in;}
.line.tall{height:.3in;}
.box{border:.75pt solid var(--rule);height:.42in;}
.checks{display:flex;flex-wrap:wrap;gap:.05in .16in;font-size:7.4pt;color:var(--ink);}
.ck{display:flex;align-items:center;gap:.045in;}
.ck i{width:.105in;height:.105in;border:.9pt solid var(--navy);display:inline-block;}
.orders{background:#F4F6F8;border-left:2.5pt solid var(--slate);
  padding:.09in .11in;margin-bottom:.115in;}
.freq{display:flex;align-items:baseline;gap:.05in;font-size:7.6pt;margin-top:.07in;}
.freq .in{border-bottom:.75pt solid var(--rule);width:.42in;display:inline-block;height:.14in;}
.clin{margin-top:auto;background:#F4F6F8;padding:.085in .11in;margin-bottom:.11in;}
.clin .who{display:flex;gap:.2in;margin-top:.05in;}
.clin .who div{font-size:7.2pt;line-height:1.35;}
.clin .who b{color:var(--navy);}
.clin .who span{display:block;font-size:6.4pt;color:var(--muted);
  letter-spacing:.06em;text-transform:uppercase;}
.clin .tech{font-size:6.6pt;color:var(--muted);margin-top:.06in;line-height:1.4;}
.sig{border-top:.75pt solid var(--rule);padding-top:.1in;}
.foot{margin-top:.1in;border-top:2.5pt solid var(--navy);padding-top:.07in;
  display:flex;justify-content:space-between;align-items:flex-end;gap:.12in;}
.foot .addr{font-size:6.6pt;line-height:1.45;color:var(--muted);}
.foot .addr b{color:var(--navy);}
.foot .send{text-align:right;font-size:6.6pt;line-height:1.45;color:var(--muted);}
.tofill{color:#C0392B;}
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
  <div class="freq">
    <span></span><span class="in"></span> visits per week for
    <span class="in"></span> weeks
    &nbsp;&nbsp;&nbsp; Re-evaluate in <span class="in"></span> weeks
  </div>
</div>

<div class="grp">
  <div class="f"><label>Precautions, weight bearing status, or restrictions</label>
  <div class="box"></div></div>
</div>

<div class="clin">
  <span class="eyebrow">Treating clinicians</span>
  <div class="who">
    <div><b>Cameron Elliott, PT, MPT</b><span>Physical Therapist</span></div>
    <div><b>Jeff Cotten, PTA, ATC, LMT</b><span>Physical Therapist Assistant</span></div>
  </div>
  <div class="tech">Integrative dry needling (CIDN), Active Release Techniques,
    Primal Reflex Release, Fascial Manipulation, orthotic intervention.</div>
</div>

<div class="sig">
  <span class="eyebrow" style="display:block;margin-bottom:.06in">Referring provider</span>
  <div class="row">
    <div class="f" style="flex:2"><label>Name</label><div class="line"></div></div>
    <div class="f"><label>NPI</label><div class="line"></div></div>
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
    Phone (334) 319-1684 &nbsp;|&nbsp; Fax <span class="tofill">[FAX]</span>
  </div>
  <div class="send">
    Fax this form, or send it with your patient.<br>
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
.top img{width:2.35in;}
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
.tofill{color:#C0392B;}
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
  Seventy-five minute evaluations, forty-five minute follow-ups, and four
  treatment rooms, so your patient is seen promptly and treated by the same
  clinician each visit.
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
      <li>Custom orthotic assessment</li>
    </ul>
  </div>
</div>

<div class="why">
  <h2>Why refer here</h2>
  <div class="three">
    <div><b>Prompt access</b><p>We contact every referral within one business day
      and work to see new patients quickly, so your patient does not wait weeks
      to start.</p></div>
    <div><b>Real hands-on time</b><p>Seventy-five minutes for an evaluation and
      forty-five for follow-ups, delivered by a licensed clinician rather than
      handed off to aides.</p></div>
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
    <b>Jeff Cotten, PTA, ATC, LMT</b><span>Physical Therapist Assistant</span>
    <p>Nearly 30 years across outpatient orthopedics, manual therapy and sports
      medicine. Certified athletic trainer, licensed massage therapist, CIDN, ART.</p>
  </div>
</div>

<div class="strip">
  <div><b>Insurance</b><p>Blue Cross Blue Shield, Tricare, Medicaid, Humana,
    United Healthcare, workers compensation, and self pay.</p></div>
  <div><b>Hours</b><p>Mon and Wed 7:30 to 4:30<br>Tue and Thu 9:00 to 6:00<br>
    Fri 7:30 to 12:00</p></div>
  <div><b>How to refer</b><p>Fax the referral form, call the clinic, or send your
    patient with a referral slip from our pad.</p></div>
</div>

<div class="foot">
  <div class="a"><b>Corrective Bodyworks Rehabilitation &amp; Wellness</b>
    17257 Highway 49 South, Notasulga, AL 36866<br>
    jeff@correctiverehab.com</div>
  <div class="cta">Referrals and questions<br><b>(334) 319-1684</b>
    Fax <span class="tofill">[FAX]</span></div>
</div>
""" % {'logo': LOGO}

write('physician-flyer.html', flyer_css, flyer_body)
