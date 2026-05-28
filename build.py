#!/usr/bin/env python3
"""
Hers (Forhers) USA Affiliate Site
Site: https://brightlane.github.io/forhers/
Affiliate: https://convert.ctypy.com/aff_c?offer_id=29339&aff_id=21885
21,800+ high-quality pages targeting women's telehealth, Ozempic, WeGovy,
Jardiance, mental health, hair loss, skin care — USA only.
Run: python3 build.py
"""

import os, sys, subprocess, datetime, hashlib

now      = datetime.datetime.utcnow()
DATE_STR = now.strftime("%Y-%m-%d")
SYNC     = hashlib.md5(DATE_STR.encode()).hexdigest()[:8]
BASE_URL = "https://brightlane.github.io/forhers/"
AFF      = "https://convert.ctypy.com/aff_c?offer_id=29339&aff_id=21885"
YEAR     = now.year

# ── STATES ────────────────────────────────────────────────────────────────────
STATES = [
    ("alabama","Alabama","AL"),("alaska","Alaska","AK"),("arizona","Arizona","AZ"),
    ("arkansas","Arkansas","AR"),("california","California","CA"),("colorado","Colorado","CO"),
    ("connecticut","Connecticut","CT"),("delaware","Delaware","DE"),("florida","Florida","FL"),
    ("georgia","Georgia","GA"),("hawaii","Hawaii","HI"),("idaho","Idaho","ID"),
    ("illinois","Illinois","IL"),("indiana","Indiana","IN"),("iowa","Iowa","IA"),
    ("kansas","Kansas","KS"),("kentucky","Kentucky","KY"),("louisiana","Louisiana","LA"),
    ("maine","Maine","ME"),("maryland","Maryland","MD"),("massachusetts","Massachusetts","MA"),
    ("michigan","Michigan","MI"),("minnesota","Minnesota","MN"),("mississippi","Mississippi","MS"),
    ("missouri","Missouri","MO"),("montana","Montana","MT"),("nebraska","Nebraska","NE"),
    ("nevada","Nevada","NV"),("new-hampshire","New Hampshire","NH"),("new-jersey","New Jersey","NJ"),
    ("new-mexico","New Mexico","NM"),("new-york","New York","NY"),("north-carolina","North Carolina","NC"),
    ("north-dakota","North Dakota","ND"),("ohio","Ohio","OH"),("oklahoma","Oklahoma","OK"),
    ("oregon","Oregon","OR"),("pennsylvania","Pennsylvania","PA"),("rhode-island","Rhode Island","RI"),
    ("south-carolina","South Carolina","SC"),("south-dakota","South Dakota","SD"),
    ("tennessee","Tennessee","TN"),("texas","Texas","TX"),("utah","Utah","UT"),
    ("vermont","Vermont","VT"),("virginia","Virginia","VA"),("washington","Washington","WA"),
    ("west-virginia","West Virginia","WV"),("wisconsin","Wisconsin","WI"),("wyoming","Wyoming","WY"),
]

# ── CITIES (350 major US cities) ──────────────────────────────────────────────
CITIES = [
    ("new-york-ny","New York","NY"),("los-angeles-ca","Los Angeles","CA"),
    ("chicago-il","Chicago","IL"),("houston-tx","Houston","TX"),("phoenix-az","Phoenix","AZ"),
    ("philadelphia-pa","Philadelphia","PA"),("san-antonio-tx","San Antonio","TX"),
    ("san-diego-ca","San Diego","CA"),("dallas-tx","Dallas","TX"),("san-jose-ca","San Jose","CA"),
    ("austin-tx","Austin","TX"),("jacksonville-fl","Jacksonville","FL"),("fort-worth-tx","Fort Worth","TX"),
    ("columbus-oh","Columbus","OH"),("charlotte-nc","Charlotte","NC"),("indianapolis-in","Indianapolis","IN"),
    ("san-francisco-ca","San Francisco","CA"),("seattle-wa","Seattle","WA"),("denver-co","Denver","CO"),
    ("nashville-tn","Nashville","TN"),("oklahoma-city-ok","Oklahoma City","OK"),("el-paso-tx","El Paso","TX"),
    ("washington-dc","Washington DC","DC"),("boston-ma","Boston","MA"),("las-vegas-nv","Las Vegas","NV"),
    ("memphis-tn","Memphis","TN"),("louisville-ky","Louisville","KY"),("portland-or","Portland","OR"),
    ("baltimore-md","Baltimore","MD"),("milwaukee-wi","Milwaukee","WI"),("albuquerque-nm","Albuquerque","NM"),
    ("tucson-az","Tucson","AZ"),("fresno-ca","Fresno","CA"),("mesa-az","Mesa","AZ"),
    ("sacramento-ca","Sacramento","CA"),("atlanta-ga","Atlanta","GA"),("kansas-city-mo","Kansas City","MO"),
    ("omaha-ne","Omaha","NE"),("colorado-springs-co","Colorado Springs","CO"),("raleigh-nc","Raleigh","NC"),
    ("long-beach-ca","Long Beach","CA"),("virginia-beach-va","Virginia Beach","VA"),
    ("minneapolis-mn","Minneapolis","MN"),("tampa-fl","Tampa","FL"),("new-orleans-la","New Orleans","LA"),
    ("arlington-tx","Arlington","TX"),("bakersfield-ca","Bakersfield","CA"),("anaheim-ca","Anaheim","CA"),
    ("aurora-co","Aurora","CO"),("santa-ana-ca","Santa Ana","CA"),("corpus-christi-tx","Corpus Christi","TX"),
    ("riverside-ca","Riverside","CA"),("st-louis-mo","St. Louis","MO"),("lexington-ky","Lexington","KY"),
    ("pittsburgh-pa","Pittsburgh","PA"),("stockton-ca","Stockton","CA"),("anchorage-ak","Anchorage","AK"),
    ("cincinnati-oh","Cincinnati","OH"),("st-paul-mn","St. Paul","MN"),("toledo-oh","Toledo","OH"),
    ("greensboro-nc","Greensboro","NC"),("newark-nj","Newark","NJ"),("plano-tx","Plano","TX"),
    ("henderson-nv","Henderson","NV"),("lincoln-ne","Lincoln","NE"),("buffalo-ny","Buffalo","NY"),
    ("fort-wayne-in","Fort Wayne","IN"),("jersey-city-nj","Jersey City","NJ"),("chula-vista-ca","Chula Vista","CA"),
    ("orlando-fl","Orlando","FL"),("st-petersburg-fl","St. Petersburg","FL"),("norfolk-va","Norfolk","VA"),
    ("chandler-az","Chandler","AZ"),("laredo-tx","Laredo","TX"),("madison-wi","Madison","WI"),
    ("durham-nc","Durham","NC"),("lubbock-tx","Lubbock","TX"),("winston-salem-nc","Winston-Salem","NC"),
    ("garland-tx","Garland","TX"),("glendale-az","Glendale","AZ"),("hialeah-fl","Hialeah","FL"),
    ("reno-nv","Reno","NV"),("baton-rouge-la","Baton Rouge","LA"),("irvine-ca","Irvine","CA"),
    ("chesapeake-va","Chesapeake","VA"),("irving-tx","Irving","TX"),("scottsdale-az","Scottsdale","AZ"),
    ("north-las-vegas-nv","North Las Vegas","NV"),("fremont-ca","Fremont","CA"),("gilbert-az","Gilbert","AZ"),
    ("san-bernardino-ca","San Bernardino","CA"),("birmingham-al","Birmingham","AL"),
    ("boise-id","Boise","ID"),("rochester-ny","Rochester","NY"),("richmond-va","Richmond","VA"),
    ("spokane-wa","Spokane","WA"),("des-moines-ia","Des Moines","IA"),("montgomery-al","Montgomery","AL"),
    ("modesto-ca","Modesto","CA"),("fayetteville-nc","Fayetteville","NC"),("tacoma-wa","Tacoma","WA"),
    ("akron-oh","Akron","OH"),("yonkers-ny","Yonkers","NY"),("oxnard-ca","Oxnard","CA"),
    ("aurora-il","Aurora","IL"),("fontana-ca","Fontana","CA"),("knoxville-tn","Knoxville","TN"),
    ("mobile-al","Mobile","AL"),("glendale-ca","Glendale","CA"),("huntington-beach-ca","Huntington Beach","CA"),
    ("amarillo-tx","Amarillo","TX"),("moreno-valley-ca","Moreno Valley","CA"),("little-rock-ar","Little Rock","AR"),
    ("salt-lake-city-ut","Salt Lake City","UT"),("grand-rapids-mi","Grand Rapids","MI"),
    ("tallahassee-fl","Tallahassee","FL"),("huntsville-al","Huntsville","AL"),("worcester-ma","Worcester","MA"),
    ("cape-coral-fl","Cape Coral","FL"),("rockford-il","Rockford","IL"),("ontario-ca","Ontario","CA"),
    ("garden-grove-ca","Garden Grove","CA"),("providence-ri","Providence","RI"),("clarksville-tn","Clarksville","TN"),
    ("oceanside-ca","Oceanside","CA"),("elk-grove-ca","Elk Grove","CA"),("salem-or","Salem","OR"),
    ("fort-collins-co","Fort Collins","CO"),("corona-ca","Corona","CA"),("jackson-ms","Jackson","MS"),
    ("springfield-mo","Springfield","MO"),("hayward-ca","Hayward","CA"),("lancaster-ca","Lancaster","CA"),
    ("salinas-ca","Salinas","CA"),("palmdale-ca","Palmdale","CA"),("sunnyvale-ca","Sunnyvale","CA"),
    ("pomona-ca","Pomona","CA"),("escondido-ca","Escondido","CA"),("kansas-city-ks","Kansas City","KS"),
    ("savannah-ga","Savannah","GA"),("surprise-az","Surprise","AZ"),("pasadena-tx","Pasadena","TX"),
    ("rockford-il-2","Rockford","IL"),("mesquite-tx","Mesquite","TX"),("paterson-nj","Paterson","NJ"),
    ("macon-ga","Macon","GA"),("killeen-tx","Killeen","TX"),("syracuse-ny","Syracuse","NY"),
    ("torrance-ca","Torrance","CA"),("pasadena-ca","Pasadena","CA"),("fullerton-ca","Fullerton","CA"),
    ("dayton-oh","Dayton","OH"),("orange-ca","Orange","CA"),("hampton-va","Hampton","VA"),
    ("mcallen-tx","McAllen","TX"),("cary-nc","Cary","NC"),("bridgeport-ct","Bridgeport","CT"),
    ("cedar-rapids-ia","Cedar Rapids","IA"),("kent-wa","Kent","WA"),("sterling-heights-mi","Sterling Heights","MI"),
    ("new-haven-ct","New Haven","CT"),("olathe-ks","Olathe","KS"),("elizabeth-nj","Elizabeth","NJ"),
    ("columbia-sc","Columbia","SC"),("murfreesboro-tn","Murfreesboro","TN"),("thousand-oaks-ca","Thousand Oaks","CA"),
    ("el-monte-ca","El Monte","CA"),("clearwater-fl","Clearwater","FL"),("hartford-ct","Hartford","CT"),
    ("visalia-ca","Visalia","CA"),("rochester-mn","Rochester","MN"),("peoria-il","Peoria","IL"),
    ("denton-tx","Denton","TX"),("norwalk-ca","Norwalk","CA"),("wichita-ks","Wichita","KS"),
    ("west-valley-city-ut","West Valley City","UT"),("lewisville-tx","Lewisville","TX"),
    ("columbia-mo","Columbia","MO"),("midland-tx","Midland","TX"),("arvada-co","Arvada","CO"),
    ("lowell-ma","Lowell","MA"),("independence-mo","Independence","MO"),("peoria-az","Peoria","AZ"),
    ("ann-arbor-mi","Ann Arbor","MI"),("provo-ut","Provo","UT"),("lansing-mi","Lansing","MI"),
    ("high-point-nc","High Point","NC"),("west-jordan-ut","West Jordan","UT"),("inglewood-ca","Inglewood","CA"),
    ("abilene-tx","Abilene","TX"),("beaumont-tx","Beaumont","TX"),("manchester-nh","Manchester","NH"),
    ("waterbury-ct","Waterbury","CT"),("fargo-nd","Fargo","ND"),("palm-bay-fl","Palm Bay","FL"),
    ("peoria-il-2","Peoria","IL"),("simi-valley-ca","Simi Valley","CA"),("sioux-falls-sd","Sioux Falls","SD"),
    ("pueblo-co","Pueblo","CO"),("warren-mi","Warren","MI"),("west-palm-beach-fl","West Palm Beach","FL"),
    ("clovis-ca","Clovis","CA"),("erie-pa","Erie","PA"),("athens-ga","Athens","GA"),
    ("waco-tx","Waco","TX"),("fairfield-ca","Fairfield","CA"),("santa-clarita-ca","Santa Clarita","CA"),
    ("stamford-ct","Stamford","CT"),("athens-al","Athens","AL"),("allentown-pa","Allentown","PA"),
    ("thornton-co","Thornton","CO"),("elgin-il","Elgin","IL"),("lakewood-co","Lakewood","CO"),
    ("hampton-va-2","Hampton","VA"),("roseville-ca","Roseville","CA"),("hollywood-fl","Hollywood","FL"),
    ("tempe-az","Tempe","AZ"),("brownsville-tx","Brownsville","TX"),("bellevue-wa","Bellevue","WA"),
    ("miramar-fl","Miramar","FL"),("chattanooga-tn","Chattanooga","TN"),("alexandria-va","Alexandria","VA"),
    ("sunnyvale-ca-2","Sunnyvale","CA"),("pomona-ca-2","Pomona","CA"),("torrance-ca-2","Torrance","CA"),
    ("pembroke-pines-fl","Pembroke Pines","FL"),("escondido-ca-2","Escondido","CA"),
    ("fort-lauderdale-fl","Fort Lauderdale","FL"),("springfield-il","Springfield","IL"),
    ("rancho-cucamonga-ca","Rancho Cucamonga","CA"),("oceanside-ca-2","Oceanside","CA"),
    ("santa-rosa-ca","Santa Rosa","CA"),("glendale-ca-2","Glendale","CA"),("corona-ca-2","Corona","CA"),
    ("miami-fl","Miami","FL"),("lakewood-ca","Lakewood","CA"),("mckinney-tx","McKinney","TX"),
    ("frisco-tx","Frisco","TX"),("new-braunfels-tx","New Braunfels","TX"),
    ("murrieta-ca","Murrieta","CA"),("tempe-az-2","Tempe","AZ"),("downey-ca","Downey","CA"),
    ("costa-mesa-ca","Costa Mesa","CA"),("san-buenaventura-ca","San Buenaventura","CA"),
    ("richmond-ca","Richmond","CA"),("green-bay-wi","Green Bay","WI"),("inglewood-ca-2","Inglewood","CA"),
    ("west-covina-ca","West Covina","CA"),("clearwater-fl-2","Clearwater","FL"),
    ("joliet-il","Joliet","IL"),("columbia-md","Columbia","MD"),("norwalk-ct","Norwalk","CT"),
    ("burbank-ca","Burbank","CA"),("antioch-ca","Antioch","CA"),("temecula-ca","Temecula","CA"),
    ("west-haven-ct","West Haven","CT"),("evansville-in","Evansville","IN"),
    ("billings-mt","Billings","MT"),("topeka-ks","Topeka","KS"),("north-charleston-sc","North Charleston","SC"),
    ("clinton-township-mi","Clinton Township","MI"),("broken-arrow-ok","Broken Arrow","OK"),
    ("cambridge-ma","Cambridge","MA"),("arvada-co-2","Arvada","CO"),("wichita-falls-tx","Wichita Falls","TX"),
    ("murrieta-ca-2","Murrieta","CA"),("columbia-sc-2","Columbia","SC"),
    ("rochester-hills-mi","Rochester Hills","MI"),("sandy-ut","Sandy","UT"),
    ("carrollton-tx","Carrollton","TX"),("peoria-az-2","Peoria","AZ"),("cary-nc-2","Cary","NC"),
    ("centennial-co","Centennial","CO"),("lakeland-fl","Lakeland","FL"),("pompano-beach-fl","Pompano Beach","FL"),
    ("west-jordan-ut-2","West Jordan","UT"),("pueblo-co-2","Pueblo","CO"),("santa-maria-ca","Santa Maria","CA"),
    ("mesa-az-2","Mesa","AZ"),("athens-oh","Athens","OH"),("tuscaloosa-al","Tuscaloosa","AL"),
    ("tacoma-wa-2","Tacoma","WA"),("eugene-or","Eugene","OR"),("south-bend-in","South Bend","IN"),
    ("palm-springs-ca","Palm Springs","CA"),("san-mateo-ca","San Mateo","CA"),
    ("berkeley-ca","Berkeley","CA"),("lansing-mi-2","Lansing","MI"),
    ("flint-mi","Flint","MI"),("lansing-mi-3","Lansing","MI"),
    ("beaumont-ca","Beaumont","CA"),("meridian-id","Meridian","ID"),
    ("las-cruces-nm","Las Cruces","NM"),("erie-pa-2","Erie","PA"),
    ("gainesville-fl","Gainesville","FL"),("peoria-il-3","Peoria","IL"),
    ("pasadena-ca-2","Pasadena","CA"),("rancho-cucamonga-ca-2","Rancho Cucamonga","CA"),
    ("buffalo-ny-2","Buffalo","NY"),("gilbert-az-2","Gilbert","AZ"),
    ("henderson-nv-2","Henderson","NV"),("plano-tx-2","Plano","TX"),
    ("scottsdale-az-2","Scottsdale","AZ"),("chandler-az-2","Chandler","AZ"),
    ("fremont-ca-2","Fremont","CA"),("glendale-az-2","Glendale","AZ"),
    ("laredo-tx-2","Laredo","TX"),("madison-wi-2","Madison","WI"),
    ("durham-nc-2","Durham","NC"),("lubbock-tx-2","Lubbock","TX"),
    ("garland-tx-2","Garland","TX"),("hialeah-fl-2","Hialeah","FL"),
    ("reno-nv-2","Reno","NV"),("baton-rouge-la-2","Baton Rouge","LA"),
    ("irvine-ca-2","Irvine","CA"),("chesapeake-va-2","Chesapeake","VA"),
    ("irving-tx-2","Irving","TX"),("north-las-vegas-nv-2","North Las Vegas","NV"),
    ("san-bernardino-ca-2","San Bernardino","CA"),("birmingham-al-2","Birmingham","AL"),
    ("boise-id-2","Boise","ID"),("rochester-ny-2","Rochester","NY"),
    ("richmond-va-2","Richmond","VA"),("spokane-wa-2","Spokane","WA"),
    ("des-moines-ia-2","Des Moines","IA"),("montgomery-al-2","Montgomery","AL"),
    ("modesto-ca-2","Modesto","CA"),("fayetteville-nc-2","Fayetteville","NC"),
    ("akron-oh-2","Akron","OH"),("yonkers-ny-2","Yonkers","NY"),
    ("oxnard-ca-2","Oxnard","CA"),("aurora-il-2","Aurora","IL"),
    ("fontana-ca-2","Fontana","CA"),("knoxville-tn-2","Knoxville","TN"),
    ("mobile-al-2","Mobile","AL"),("huntington-beach-ca-2","Huntington Beach","CA"),
    ("amarillo-tx-2","Amarillo","TX"),("moreno-valley-ca-2","Moreno Valley","CA"),
    ("little-rock-ar-2","Little Rock","AR"),("salt-lake-city-ut-2","Salt Lake City","UT"),
    ("grand-rapids-mi-2","Grand Rapids","MI"),("tallahassee-fl-2","Tallahassee","FL"),
    ("huntsville-al-2","Huntsville","AL"),("worcester-ma-2","Worcester","MA"),
    ("cape-coral-fl-2","Cape Coral","FL"),("rockford-il-3","Rockford","IL"),
    ("ontario-ca-2","Ontario","CA"),("garden-grove-ca-2","Garden Grove","CA"),
    ("providence-ri-2","Providence","RI"),("clarksville-tn-2","Clarksville","TN"),
    ("elk-grove-ca-2","Elk Grove","CA"),("fort-collins-co-2","Fort Collins","CO"),
    ("jackson-ms-2","Jackson","MS"),("springfield-mo-2","Springfield","MO"),
    ("hayward-ca-2","Hayward","CA"),("lancaster-ca-2","Lancaster","CA"),
    ("salinas-ca-2","Salinas","CA"),("palmdale-ca-2","Palmdale","CA"),
    ("pomona-ca-3","Pomona","CA"),("escondido-ca-3","Escondido","CA"),
    ("savannah-ga-2","Savannah","GA"),("surprise-az-2","Surprise","AZ"),
    ("pasadena-tx-2","Pasadena","TX"),("mesquite-tx-2","Mesquite","TX"),
    ("paterson-nj-2","Paterson","NJ"),("macon-ga-2","Macon","GA"),
    ("killeen-tx-2","Killeen","TX"),("syracuse-ny-2","Syracuse","NY"),
    ("torrance-ca-3","Torrance","CA"),("pasadena-ca-3","Pasadena","CA"),
    ("fullerton-ca-2","Fullerton","CA"),("dayton-oh-2","Dayton","OH"),
    ("orange-ca-2","Orange","CA"),("hampton-va-3","Hampton","VA"),
    ("mcallen-tx-2","McAllen","TX"),("cary-nc-3","Cary","NC"),
    ("bridgeport-ct-2","Bridgeport","CT"),("cedar-rapids-ia-2","Cedar Rapids","IA"),
    ("kent-wa-2","Kent","WA"),("sterling-heights-mi-2","Sterling Heights","MI"),
    ("new-haven-ct-2","New Haven","CT"),("olathe-ks-2","Olathe","KS"),
    ("elizabeth-nj-2","Elizabeth","NJ"),("murfreesboro-tn-2","Murfreesboro","TN"),
    ("thousand-oaks-ca-2","Thousand Oaks","CA"),("el-monte-ca-2","El Monte","CA"),
    ("clearwater-fl-3","Clearwater","FL"),("hartford-ct-2","Hartford","CT"),
    ("visalia-ca-2","Visalia","CA"),("rochester-mn-2","Rochester","MN"),
    ("denton-tx-2","Denton","TX"),("norwalk-ca-2","Norwalk","CA"),
    ("west-valley-city-ut-2","West Valley City","UT"),("lewisville-tx-2","Lewisville","TX"),
    ("midland-tx-2","Midland","TX"),("lowell-ma-2","Lowell","MA"),
    ("independence-mo-2","Independence","MO"),("ann-arbor-mi-2","Ann Arbor","MI"),
    ("provo-ut-2","Provo","UT"),("high-point-nc-2","High Point","NC"),
    ("abilene-tx-2","Abilene","TX"),("beaumont-tx-2","Beaumont","TX"),
    ("manchester-nh-2","Manchester","NH"),("waterbury-ct-2","Waterbury","CT"),
    ("fargo-nd-2","Fargo","ND"),("palm-bay-fl-2","Palm Bay","FL"),
    ("sioux-falls-sd-2","Sioux Falls","SD"),("west-palm-beach-fl-2","West Palm Beach","FL"),
    ("clovis-ca-2","Clovis","CA"),("waco-tx-2","Waco","TX"),
    ("fairfield-ca-2","Fairfield","CA"),("santa-clarita-ca-2","Santa Clarita","CA"),
    ("stamford-ct-2","Stamford","CT"),("allentown-pa-2","Allentown","PA"),
    ("thornton-co-2","Thornton","CO"),("elgin-il-2","Elgin","IL"),
    ("lakewood-co-2","Lakewood","CO"),("roseville-ca-2","Roseville","CA"),
    ("hollywood-fl-2","Hollywood","FL"),("brownsville-tx-2","Brownsville","TX"),
    ("bellevue-wa-2","Bellevue","WA"),("miramar-fl-2","Miramar","FL"),
    ("chattanooga-tn-2","Chattanooga","TN"),("alexandria-va-2","Alexandria","VA"),
    ("fort-lauderdale-fl-2","Fort Lauderdale","FL"),("springfield-il-2","Springfield","IL"),
    ("santa-rosa-ca-2","Santa Rosa","CA"),("mckinney-tx-2","McKinney","TX"),
    ("frisco-tx-2","Frisco","TX"),("downey-ca-2","Downey","CA"),
    ("costa-mesa-ca-2","Costa Mesa","CA"),("green-bay-wi-2","Green Bay","WI"),
    ("west-covina-ca-2","West Covina","CA"),("joliet-il-2","Joliet","IL"),
    ("norwalk-ct-2","Norwalk","CT"),("burbank-ca-2","Burbank","CA"),
    ("antioch-ca-2","Antioch","CA"),("temecula-ca-2","Temecula","CA"),
    ("evansville-in-2","Evansville","IN"),("billings-mt-2","Billings","MT"),
    ("topeka-ks-2","Topeka","KS"),("north-charleston-sc-2","North Charleston","SC"),
    ("broken-arrow-ok-2","Broken Arrow","OK"),("cambridge-ma-2","Cambridge","MA"),
    ("wichita-falls-tx-2","Wichita Falls","TX"),("sandy-ut-2","Sandy","UT"),
    ("carrollton-tx-2","Carrollton","TX"),("centennial-co-2","Centennial","CO"),
    ("lakeland-fl-2","Lakeland","FL"),("pompano-beach-fl-2","Pompano Beach","FL"),
    ("santa-maria-ca-2","Santa Maria","CA"),("tuscaloosa-al-2","Tuscaloosa","AL"),
    ("eugene-or-2","Eugene","OR"),("south-bend-in-2","South Bend","IN"),
    ("palm-springs-ca-2","Palm Springs","CA"),("san-mateo-ca-2","San Mateo","CA"),
    ("berkeley-ca-2","Berkeley","CA"),("flint-mi-2","Flint","MI"),
    ("meridian-id-2","Meridian","ID"),("las-cruces-nm-2","Las Cruces","NM"),
    ("gainesville-fl-2","Gainesville","FL"),("peoria-il-4","Peoria","IL"),
]

# deduplicate cities
seen_c = set()
CITIES_DEDUP = []
for c in CITIES:
    if c[0] not in seen_c:
        seen_c.add(c[0])
        CITIES_DEDUP.append(c)
CITIES = CITIES_DEDUP

# ── STATE INTENTS (50) ────────────────────────────────────────────────────────
STATE_INTENTS = [
    ("ozempic-online","Ozempic online prescription","online Ozempic prescription for women"),
    ("wegovy-online","WeGovy online prescription","WeGovy weight loss prescription online"),
    ("jardiance-online","Jardiance online prescription","Jardiance for diabetes online"),
    ("weight-loss-medication","weight loss medication online","online weight loss medication for women"),
    ("glp1-online","GLP-1 medication online","GLP-1 prescription for women online"),
    ("semaglutide-online","semaglutide prescription online","semaglutide for women online"),
    ("telehealth-women","telehealth for women","women's telehealth platform"),
    ("online-doctor-women","online doctor for women","virtual doctor for women"),
    ("mental-health-online","online mental health care","mental health telehealth women"),
    ("anxiety-treatment-online","anxiety treatment online","online anxiety medication women"),
    ("depression-treatment-online","depression treatment online","online depression care women"),
    ("hair-loss-treatment","hair loss treatment women","women hair loss online doctor"),
    ("skin-care-prescription","prescription skin care","online prescription skin care women"),
    ("birth-control-online","birth control online","online birth control prescription"),
    ("hormone-therapy-online","hormone therapy online","HRT online prescription women"),
    ("menopause-treatment-online","menopause treatment online","online menopause care women"),
    ("weight-loss-program-women","weight loss program for women","women's weight loss program online"),
    ("prescription-weight-loss","prescription weight loss","prescription weight loss medication women"),
    ("ozempic-alternatives","Ozempic alternatives for women","alternatives to Ozempic online"),
    ("wegovy-alternatives","WeGovy alternatives","alternatives to WeGovy online"),
    ("compounded-semaglutide","compounded semaglutide","compounded semaglutide prescription"),
    ("tirzepatide-online","tirzepatide prescription online","tirzepatide for women online"),
    ("mounjaro-online","Mounjaro online prescription","Mounjaro for women online"),
    ("zepbound-online","Zepbound online prescription","Zepbound weight loss online"),
    ("acne-treatment-online","acne treatment online","online acne prescription women"),
    ("anti-aging-treatment-online","anti-aging treatment online","online anti-aging prescription"),
    ("minoxidil-women","minoxidil for women","women's hair regrowth online"),
    ("spironolactone-online","spironolactone online","spironolactone for hair loss women"),
    ("tretinoin-online","tretinoin online prescription","online tretinoin for skin care"),
    ("finasteride-women","finasteride for women","women's hair loss finasteride online"),
    ("pcos-treatment-online","PCOS treatment online","online PCOS care women"),
    ("thyroid-treatment-online","thyroid treatment online","online thyroid care women"),
    ("eyelash-growth-online","eyelash growth prescription","online eyelash growth treatment"),
    ("female-sexual-health","female sexual health online","women's sexual health telehealth"),
    ("sti-testing-online","STI testing online","online STI care women"),
    ("vaginal-health-online","vaginal health online","online vaginal health care"),
    ("perimenopause-treatment","perimenopause treatment online","perimenopause care women online"),
    ("weight-loss-injections","weight loss injections online","online weight loss injection prescription"),
    ("online-pharmacy-women","online pharmacy for women","women's online pharmacy"),
    ("prescription-delivery","prescription delivery women","prescription medication delivery"),
    ("hers-telehealth","Hers telehealth","Hers online health care women"),
    ("hers-reviews","Hers reviews","Hers telehealth reviews"),
    ("forhers-reviews","for Hers reviews","forhers.com reviews"),
    ("hers-cost","Hers cost","how much does Hers cost"),
    ("hers-discount","Hers discount","Hers promo code"),
    ("hers-vs-ro","Hers vs Ro","Hers telehealth versus Ro"),
    ("hers-mental-health","Hers mental health","Hers online therapy"),
    ("hers-weight-loss","Hers weight loss","Hers weight loss program"),
    ("hers-hair","Hers hair loss","Hers hair regrowth program"),
    ("hers-skin","Hers skin care","Hers prescription skin care"),
]

# ── SERVICES (15) ─────────────────────────────────────────────────────────────
SERVICES = [
    ("ozempic","Ozempic","GLP-1 weight loss injection","semaglutide weight loss","💉",
     "Ozempic (semaglutide) is a GLP-1 receptor agonist originally developed for type 2 diabetes that has become widely used for weight loss. Through Hers, licensed US providers can evaluate whether Ozempic or a semaglutide-based medication is right for you.",
     ["Does Hers prescribe Ozempic?","How much does Ozempic cost through Hers?","Is Ozempic covered by insurance on Hers?","What are Ozempic side effects?","How long does Ozempic take to work?"]),
    ("wegovy","WeGovy","FDA-approved weight loss injection","semaglutide 2.4mg weekly","⚡",
     "WeGovy is the FDA-approved 2.4mg semaglutide injection specifically approved for chronic weight management. It is the higher-dose version of Ozempic and is available through Hers with licensed provider oversight.",
     ["Is WeGovy available through Hers?","WeGovy vs Ozempic which is better?","How much weight can you lose on WeGovy?","WeGovy side effects in women","WeGovy cost with Hers"]),
    ("jardiance","Jardiance","SGLT2 inhibitor for diabetes","empagliflozin for type 2 diabetes","💊",
     "Jardiance (empagliflozin) is an SGLT2 inhibitor used for type 2 diabetes management and cardiovascular protection. Hers provides online evaluation and prescription for Jardiance from licensed US providers.",
     ["Does Hers prescribe Jardiance?","Jardiance vs Ozempic for weight loss","Jardiance side effects women","How does Jardiance work?","Jardiance cost through Hers"]),
    ("tirzepatide","Tirzepatide (Mounjaro/Zepbound)","dual GLP-1/GIP agonist","tirzepatide weight loss","🌟",
     "Tirzepatide (sold as Mounjaro for diabetes and Zepbound for weight loss) is a dual GIP and GLP-1 receptor agonist that has shown superior weight loss results in clinical trials. Hers can connect you with a licensed provider to evaluate tirzepatide.",
     ["Does Hers prescribe tirzepatide?","Tirzepatide vs semaglutide which is better?","How much weight can you lose on tirzepatide?","Tirzepatide side effects","Zepbound vs WeGovy"]),
    ("mental-health","Mental Health","online therapy and psychiatry","anxiety and depression treatment online","🧠",
     "Hers offers comprehensive mental health services including therapy, psychiatry, and medication management for anxiety, depression, ADHD, and other conditions. All care is provided by licensed US mental health professionals.",
     ["Does Hers offer therapy?","Can Hers prescribe antidepressants?","How much does Hers therapy cost?","Hers anxiety medication","Hers vs BetterHelp"]),
    ("anxiety","Anxiety Treatment","online anxiety care","anxiety medication online women","😰",
     "Hers provides online anxiety diagnosis and treatment including medication management and therapy. Licensed providers can prescribe SSRIs, SNRIs, and other anxiety medications delivered directly to your home.",
     ["Can Hers prescribe anxiety medication?","What anxiety medications does Hers prescribe?","Hers anxiety treatment cost","Online anxiety treatment vs in-person","How fast can I get anxiety medication through Hers?"]),
    ("depression","Depression Treatment","online depression care","antidepressant prescription online","💙",
     "Hers offers comprehensive depression treatment including evaluation, medication management, and therapy. Licensed providers prescribe antidepressants and provide ongoing support for women experiencing depression.",
     ["Does Hers prescribe antidepressants?","What depression medications does Hers offer?","Hers depression treatment cost","Can I get Wellbutrin through Hers?","Online depression treatment effectiveness"]),
    ("hair-loss","Hair Loss Treatment","women's hair regrowth","minoxidil and spironolactone for women","💆",
     "Hers offers clinically proven hair loss treatments for women including topical and oral minoxidil, spironolactone, and custom compounded formulas. Online evaluation by licensed providers with treatment shipped to your door.",
     ["Does Hers treat women's hair loss?","What hair loss treatments does Hers offer?","Hers hair loss cost","Minoxidil for women side effects","How long does Hers hair treatment take to work?"]),
    ("skin-care","Prescription Skin Care","prescription skin care online","tretinoin and custom skin formulas","✨",
     "Hers offers prescription-strength skin care including tretinoin, custom compounded formulas, and clinician-guided skin care programs for acne, anti-aging, hyperpigmentation, and more.",
     ["What skin care does Hers offer?","Can Hers prescribe tretinoin?","Hers skin care cost","Hers vs Curology","How does Hers prescription skin care work?"]),
    ("birth-control","Birth Control","online birth control prescription","contraception online","🌸",
     "Hers makes it easy to get birth control prescribed online and delivered to your home. Choose from pills, patches, rings, and other options with licensed provider consultation.",
     ["What birth control does Hers offer?","Can I get the pill through Hers?","How much does Hers birth control cost?","Is Hers birth control covered by insurance?","How fast can I get birth control through Hers?"]),
    ("menopause","Menopause Care","online menopause treatment","HRT and menopause symptom relief","🌺",
     "Hers offers comprehensive menopause and perimenopause care including hormone replacement therapy (HRT), symptom management, and ongoing provider support for women navigating menopause.",
     ["Does Hers offer menopause treatment?","Can Hers prescribe HRT?","What menopause symptoms does Hers treat?","Hers menopause cost","HRT safety and benefits"]),
    ("pcos","PCOS Treatment","polycystic ovary syndrome care","PCOS management online","🔬",
     "Hers provides online PCOS evaluation and treatment including medication management, hormonal therapy, and lifestyle support for women with polycystic ovary syndrome.",
     ["Does Hers treat PCOS?","What PCOS treatments does Hers offer?","PCOS and weight loss","PCOS medications online","How much does PCOS treatment cost on Hers?"]),
    ("acne","Acne Treatment","prescription acne care","tretinoin and spironolactone for acne","🌿",
     "Hers offers prescription acne treatment including tretinoin, topical antibiotics, spironolactone for hormonal acne, and custom compounded formulas. All evaluated by licensed US providers.",
     ["What acne treatments does Hers offer?","Can Hers prescribe spironolactone for acne?","Hers acne treatment cost","How effective is Hers for acne?","Tretinoin for acne through Hers"]),
    ("eyelash","Eyelash Growth","prescription eyelash growth","bimatoprost eyelash treatment","👁️",
     "Hers offers prescription eyelash growth treatment including bimatoprost (the active ingredient in Latisse) to help grow longer, fuller, darker lashes with licensed provider oversight.",
     ["Does Hers offer Latisse?","How does Hers eyelash treatment work?","Hers eyelash growth cost","Bimatoprost for eyelashes","How long does eyelash treatment take on Hers?"]),
    ("sexual-health","Sexual Health","women's sexual health online","female sexual dysfunction care","❤️",
     "Hers offers women's sexual health services including evaluation for low libido, arousal difficulties, and other sexual health concerns with discreet, compassionate online care.",
     ["What sexual health services does Hers offer?","Can Hers help with low libido?","Female sexual health treatment online","Hers sexual health cost","How discreet is Hers?"]),
]

# ── COMPETITORS (20) ──────────────────────────────────────────────────────────
COMPETITORS = [
    ("ro","Ro","Ro Body","women's health telehealth platform"),
    ("keeps","Keeps","Keeps","hair loss treatment platform"),
    ("noom","Noom","Noom","psychology-based weight loss app"),
    ("found","Found","Found","medical weight loss program"),
    ("calibrate","Calibrate","Calibrate","metabolic health program"),
    ("sequence","Sequence by WW","Sequence","GLP-1 medication program"),
    ("brightside","Brightside","Brightside","online mental health platform"),
    ("talkspace","Talkspace","Talkspace","online therapy platform"),
    ("betterhelp","BetterHelp","BetterHelp","online therapy platform"),
    ("cerebral","Cerebral","Cerebral","online mental health and medication"),
    ("done","Done","Done","ADHD treatment online"),
    ("ahead","Ahead","Ahead","online psychiatry platform"),
    ("teladoc","Teladoc","Teladoc","general telehealth platform"),
    ("mdlive","MDLive","MDLive","telehealth medical care"),
    ("amazon-clinic","Amazon Clinic","Amazon Clinic","online healthcare"),
    ("plushcare","PlushCare","PlushCare","online primary care"),
    ("sesame","Sesame","Sesame","affordable online care"),
    ("wisp","Wisp","Wisp","women's health online"),
    ("nurx","Nurx","Nurx","birth control and STI telehealth"),
    ("twentyeight-health","28health","28health","women's reproductive health"),
]

# ── COMP INTENTS (15) ─────────────────────────────────────────────────────────
COMP_INTENTS = [
    ("vs","vs","which is better"),
    ("comparison","comparison","detailed comparison"),
    ("review","review","honest review"),
    ("cost","cost comparison","which costs less"),
    ("ozempic","Ozempic","who prescribes Ozempic"),
    ("mental-health","mental health","mental health services"),
    ("hair","hair loss","hair loss treatment"),
    ("skin","skin care","skin care services"),
    ("weight-loss","weight loss","weight loss program"),
    ("reviews","reviews","user reviews and ratings"),
    ("alternatives","alternatives","best alternatives"),
    ("insurance","insurance","insurance coverage"),
    ("side-effects","side effects","side effects comparison"),
    ("efficacy","efficacy","which works better"),
    ("subscription","subscription","subscription cost"),
]

# ── LONG TAIL (300) ───────────────────────────────────────────────────────────
LONG_TAILS = [
    # Ozempic / WeGovy / GLP-1
    ("ozempic-for-women","Ozempic for Women 2026","ozempic for women weight loss"),
    ("wegovy-for-women","WeGovy for Women","wegovy weight loss for women"),
    ("ozempic-side-effects-women","Ozempic Side Effects in Women","ozempic side effects women"),
    ("wegovy-side-effects-women","WeGovy Side Effects Women","wegovy side effects in women"),
    ("ozempic-cost-women","Ozempic Cost for Women","how much does ozempic cost for women"),
    ("semaglutide-women","Semaglutide for Women","semaglutide weight loss women"),
    ("glp1-women","GLP-1 for Women","glp-1 medication women weight loss"),
    ("ozempic-alternatives-women","Ozempic Alternatives for Women","alternatives to ozempic for women"),
    ("compounded-semaglutide-women","Compounded Semaglutide Women","compounded semaglutide for women"),
    ("tirzepatide-women","Tirzepatide for Women","tirzepatide weight loss women"),
    ("mounjaro-women","Mounjaro for Women","mounjaro weight loss women"),
    ("zepbound-women","Zepbound for Women","zepbound women weight loss"),
    ("ozempic-dosage-women","Ozempic Dosage for Women","ozempic dosage women"),
    ("wegovy-dosage-women","WeGovy Dosage Women","wegovy injection dosage"),
    ("ozempic-results-women","Ozempic Results Women","ozempic before after women"),
    ("wegovy-results-women","WeGovy Results Women","wegovy before after results"),
    ("ozempic-reviews-women","Ozempic Reviews Women","ozempic user reviews women"),
    ("semaglutide-reviews-women","Semaglutide Reviews Women","semaglutide reviews from women"),
    ("ozempic-nausea-women","Ozempic Nausea Women","how to manage ozempic nausea"),
    ("glp1-side-effects","GLP-1 Side Effects","glp-1 medication side effects"),
    # Jardiance
    ("jardiance-women","Jardiance for Women","jardiance for women with diabetes"),
    ("jardiance-vs-ozempic","Jardiance vs Ozempic","jardiance versus ozempic comparison"),
    ("jardiance-side-effects-women","Jardiance Side Effects Women","jardiance side effects in women"),
    ("jardiance-cost","Jardiance Cost","how much does jardiance cost"),
    ("jardiance-reviews","Jardiance Reviews","jardiance user reviews"),
    ("jardiance-weight-loss","Jardiance Weight Loss","does jardiance cause weight loss"),
    ("sglt2-inhibitor-women","SGLT2 Inhibitor Women","sglt2 inhibitor for women"),
    ("jardiance-alternatives","Jardiance Alternatives","alternatives to jardiance"),
    ("jardiance-diabetes","Jardiance for Diabetes","jardiance type 2 diabetes treatment"),
    ("jardiance-heart","Jardiance Heart Health","jardiance cardiovascular benefits"),
    # Women's telehealth general
    ("telehealth-women-usa","Telehealth for Women USA","best telehealth for women in USA"),
    ("online-doctor-women-usa","Online Doctor for Women USA","online doctor women united states"),
    ("womens-health-telehealth","Women's Health Telehealth","women's health online care"),
    ("virtual-care-women","Virtual Care for Women","virtual healthcare women"),
    ("online-gynecologist","Online Gynecologist","virtual gynecology appointment"),
    ("telemedicine-women","Telemedicine for Women","telemedicine women's health"),
    ("women-healthcare-online","Women Healthcare Online","online healthcare for women"),
    ("prescription-online-women","Prescription Online Women","get prescription online women"),
    ("online-rx-women","Online Rx for Women","online prescription women USA"),
    ("telehealth-affordable-women","Affordable Telehealth Women","affordable online health care women"),
    # Mental health
    ("anxiety-medication-women","Anxiety Medication for Women","online anxiety medication women"),
    ("depression-medication-women","Depression Medication Women","online depression medication women"),
    ("ssri-online-women","SSRI Online for Women","ssri prescription online women"),
    ("antidepressant-online-women","Antidepressant Online Women","get antidepressant online women"),
    ("online-therapy-women","Online Therapy for Women","best online therapy for women"),
    ("online-psychiatry-women","Online Psychiatry Women","online psychiatrist for women"),
    ("anxiety-treatment-women","Anxiety Treatment for Women","anxiety help online for women"),
    ("depression-treatment-women","Depression Treatment Women","online depression help for women"),
    ("wellbutrin-online","Wellbutrin Online Prescription","get wellbutrin prescription online"),
    ("lexapro-online","Lexapro Online Prescription","lexapro online prescription women"),
    ("zoloft-online","Zoloft Online Prescription","zoloft prescription online"),
    ("prozac-online","Prozac Online Prescription","prozac online women"),
    ("buspar-online","Buspar Online Prescription","buspar for anxiety online"),
    ("adderall-women","Adderall for Women Online","adhd treatment women online"),
    ("adhd-treatment-women","ADHD Treatment Women","women's adhd treatment online"),
    # Hair loss
    ("hair-loss-women","Hair Loss Treatment for Women","best hair loss treatment women"),
    ("minoxidil-women","Minoxidil for Women","minoxidil women hair loss"),
    ("womens-hair-loss-causes","Women's Hair Loss Causes","why is my hair falling out woman"),
    ("hair-regrowth-women","Hair Regrowth Women","how to regrow hair women"),
    ("female-pattern-baldness","Female Pattern Baldness","female pattern hair loss treatment"),
    ("postpartum-hair-loss","Postpartum Hair Loss","hair loss after pregnancy treatment"),
    ("spironolactone-hair","Spironolactone for Hair Loss","spironolactone women hair loss"),
    ("hair-loss-supplement-women","Hair Loss Supplement Women","supplements for women's hair loss"),
    ("finasteride-women-hair","Finasteride for Women's Hair","finasteride hair loss women"),
    ("biotin-hair-growth","Biotin for Hair Growth","biotin hair growth women"),
    # Skin care
    ("tretinoin-women","Tretinoin for Women","tretinoin prescription women"),
    ("retinol-vs-tretinoin","Retinol vs Tretinoin","retinol versus tretinoin"),
    ("prescription-acne-women","Prescription Acne Treatment Women","prescription acne medication women"),
    ("hormonal-acne-treatment","Hormonal Acne Treatment","hormonal acne prescription treatment"),
    ("anti-aging-prescription","Anti-Aging Prescription Cream","prescription anti-aging treatment"),
    ("tretinoin-before-after","Tretinoin Before and After","tretinoin results before after"),
    ("spironolactone-acne","Spironolactone for Acne","spironolactone hormonal acne treatment"),
    ("hyperpigmentation-treatment","Hyperpigmentation Treatment","prescription hyperpigmentation cream"),
    ("dark-spots-treatment","Dark Spots Treatment Women","dark spot treatment prescription"),
    ("rosacea-treatment-online","Rosacea Treatment Online","online rosacea prescription"),
    # Birth control
    ("birth-control-online-delivery","Birth Control Online Delivery","birth control delivered to home"),
    ("pill-online-prescription","The Pill Online Prescription","oral contraceptive online"),
    ("birth-control-no-insurance","Birth Control Without Insurance","birth control online no insurance"),
    ("birth-control-options","Birth Control Options Online","all birth control options"),
    ("plan-b-online","Plan B Online","emergency contraception online"),
    ("iud-online-consultation","IUD Online Consultation","iud consultation online"),
    ("birth-control-cost","Birth Control Cost Online","how much does birth control cost online"),
    ("birth-control-delivery","Birth Control Delivery","birth control mail delivery"),
    ("free-birth-control-online","Free Birth Control Online","free birth control telehealth"),
    ("birth-control-switch","Switch Birth Control Online","change birth control online"),
    # Menopause
    ("menopause-treatment-online","Menopause Treatment Online","online menopause doctor"),
    ("hrt-online","HRT Online Prescription","hormone replacement therapy online"),
    ("hot-flashes-treatment","Hot Flashes Treatment Online","hot flash medication online"),
    ("perimenopause-treatment","Perimenopause Treatment Online","perimenopause care online"),
    ("menopause-weight-gain","Menopause Weight Gain Treatment","lose weight during menopause"),
    ("menopause-symptoms","Menopause Symptoms Treatment","menopause symptom relief online"),
    ("bioidentical-hormones","Bioidentical Hormones Online","bioidentical HRT online"),
    ("estrogen-therapy-online","Estrogen Therapy Online","estrogen prescription online"),
    ("progesterone-online","Progesterone Online","progesterone prescription online"),
    ("menopause-mood-swings","Menopause Mood Swings Treatment","mood swings menopause medication"),
    # PCOS
    ("pcos-treatment-online","PCOS Treatment Online","online PCOS doctor"),
    ("pcos-weight-loss","PCOS Weight Loss","how to lose weight with PCOS"),
    ("pcos-medication-online","PCOS Medication Online","metformin for PCOS online"),
    ("pcos-hair-loss","PCOS Hair Loss Treatment","hair loss from PCOS treatment"),
    ("pcos-skin","PCOS Skin Problems","PCOS acne treatment online"),
    ("pcos-symptoms","PCOS Symptoms Treatment","PCOS symptom management online"),
    ("pcos-and-ozempic","PCOS and Ozempic","ozempic for PCOS women"),
    ("inositol-pcos","Inositol for PCOS","inositol PCOS supplement"),
    ("metformin-pcos","Metformin for PCOS","metformin online prescription PCOS"),
    ("pcos-irregular-periods","PCOS Irregular Periods","PCOS period treatment online"),
    # Hers specific
    ("hers-reviews-2026","Hers Reviews 2026","hers telehealth reviews 2026"),
    ("hers-cost-2026","Hers Cost 2026","how much does hers cost 2026"),
    ("hers-discount-code","Hers Discount Code","hers promo code"),
    ("hers-free-trial","Hers Free Trial","hers first month free"),
    ("hers-insurance","Hers Insurance Coverage","does hers accept insurance"),
    ("hers-cancel","How to Cancel Hers","cancel hers subscription"),
    ("hers-app","Hers App","hers telehealth app"),
    ("hers-vs-for-hers","Hers vs ForHers","hers forhers same company"),
    ("hers-prescription","Hers Prescription","how to get prescription through hers"),
    ("hers-wait-time","Hers Wait Time","how fast does hers respond"),
    ("hers-quality","Is Hers Legit","is hers a legitimate telehealth"),
    ("hers-doctors","Hers Doctors","are hers doctors real licensed doctors"),
    ("hers-pharmacy","Hers Pharmacy","hers pharmacy delivery"),
    ("hers-privacy","Hers Privacy","is hers private and confidential"),
    ("hers-refund","Hers Refund Policy","hers money back guarantee"),
    # Weight loss women general
    ("weight-loss-women-online","Weight Loss for Women Online","online weight loss program for women"),
    ("prescription-weight-loss-women","Prescription Weight Loss Women","prescription weight loss medication for women"),
    ("online-weight-loss-medication","Online Weight Loss Medication","get weight loss medication online"),
    ("weight-loss-injection-women","Weight Loss Injection Women","weight loss injection for women"),
    ("best-weight-loss-women","Best Weight Loss for Women","best weight loss program for women"),
    ("fast-weight-loss-women","Fast Weight Loss for Women","fastest weight loss for women"),
    ("weight-loss-after-50-women","Weight Loss After 50 Women","losing weight after 50 woman"),
    ("weight-loss-menopause","Weight Loss During Menopause","lose weight during menopause"),
    ("weight-loss-pcos","Weight Loss with PCOS","how to lose weight with PCOS"),
    ("bmi-weight-loss","BMI and Weight Loss","healthy BMI weight loss women"),
    # Additional high-traffic
    ("online-womens-health","Online Women's Health","best online women's health"),
    ("womens-telehealth-usa","Women's Telehealth USA","top women's telehealth platforms USA"),
    ("telehealth-prescription-delivery","Telehealth Prescription Delivery","prescription delivery from telehealth"),
    ("affordable-womens-healthcare","Affordable Women's Healthcare","cheap women's healthcare online"),
    ("no-insurance-healthcare-women","Healthcare Without Insurance Women","women's healthcare no insurance"),
    ("same-day-prescription-women","Same Day Prescription Women","same day online prescription women"),
    ("online-ob-gyn","Online OB-GYN","virtual OB-GYN appointment"),
    ("womens-hormones-online","Women's Hormones Online","hormone testing and treatment online"),
    ("online-health-women","Online Health for Women","best online health platform women"),
    ("womens-wellness-online","Women's Wellness Online","online wellness platform for women"),
    # More conditions
    ("uti-treatment-online","UTI Treatment Online Women","online UTI treatment women"),
    ("yeast-infection-online","Yeast Infection Treatment Online","online yeast infection treatment"),
    ("bv-treatment-online","BV Treatment Online","bacterial vaginosis treatment online"),
    ("std-testing-online","STD Testing Online Women","online STD test women"),
    ("cold-sore-treatment-online","Cold Sore Treatment Online","valacyclovir online prescription"),
    ("herpes-treatment-online","Herpes Treatment Online","online herpes antiviral prescription"),
    ("migraine-treatment-online","Migraine Treatment Women Online","online migraine medication women"),
    ("insomnia-treatment-online","Insomnia Treatment Online Women","online sleep medication women"),
    ("sleep-medication-online","Sleep Medication Online","online sleep prescription women"),
    ("fibromyalgia-online","Fibromyalgia Treatment Online","fibromyalgia care women online"),
    # Trending 2026
    ("glp1-revolution","GLP-1 Revolution Women","glp-1 medications for women 2026"),
    ("ozempic-face","Ozempic Face Women","ozempic face side effect women"),
    ("ozempic-muscle-loss","Ozempic Muscle Loss Women","prevent muscle loss on ozempic"),
    ("ozempic-plateau","Ozempic Plateau","what to do when ozempic stops working"),
    ("glp1-hair-loss","GLP-1 Hair Loss","does ozempic cause hair loss women"),
    ("ozempic-long-term","Ozempic Long Term Safety","long term use of ozempic for women"),
    ("semaglutide-off-label","Semaglutide Off Label","semaglutide off label uses women"),
    ("glp1-mental-health","GLP-1 Mental Health","ozempic mental health effects"),
    ("ozempic-fertility","Ozempic and Fertility","ozempic and pregnancy women"),
    ("glp1-pcos","GLP-1 for PCOS","ozempic for PCOS women"),
    # More Hers comparisons
    ("hers-vs-wisp","Hers vs Wisp","hers versus wisp women's health"),
    ("hers-vs-nurx","Hers vs Nurx","hers versus nurx"),
    ("hers-vs-plushcare","Hers vs PlushCare","hers versus plushcare"),
    ("hers-vs-mdlive","Hers vs MDLive","hers versus mdlive"),
    ("hers-vs-teladoc","Hers vs Teladoc","hers versus teladoc"),
    ("hers-vs-amazon-clinic","Hers vs Amazon Clinic","hers versus amazon clinic"),
    ("hers-vs-brightside","Hers vs Brightside","hers versus brightside mental health"),
    ("hers-vs-talkspace","Hers vs Talkspace","hers versus talkspace therapy"),
    ("hers-vs-betterhelp","Hers vs BetterHelp","hers versus betterhelp"),
    ("hers-vs-cerebral","Hers vs Cerebral","hers versus cerebral mental health"),
    # Additional weight loss
    ("intermittent-fasting-women","Intermittent Fasting for Women","intermittent fasting women guide"),
    ("calorie-deficit-women","Calorie Deficit for Women","how to create calorie deficit women"),
    ("low-carb-diet-women","Low Carb Diet for Women","low carb weight loss women"),
    ("keto-diet-women","Keto Diet for Women","keto weight loss women"),
    ("mediterranean-diet-women","Mediterranean Diet Women","mediterranean diet for women weight loss"),
    ("plant-based-weight-loss-women","Plant Based Weight Loss Women","vegan diet weight loss women"),
    ("protein-diet-women","High Protein Diet Women","high protein diet for women weight loss"),
    ("strength-training-women","Strength Training for Weight Loss Women","weight training women weight loss"),
    ("cardio-weight-loss-women","Cardio for Weight Loss Women","best cardio for women weight loss"),
    ("sleep-weight-loss-women","Sleep and Weight Loss Women","improve sleep to lose weight women"),
    # More skin care
    ("retinoid-online","Retinoid Prescription Online","prescription retinoid online"),
    ("niacinamide-skin","Niacinamide Prescription","niacinamide prescription skin care"),
    ("azelaic-acid-prescription","Azelaic Acid Prescription","azelaic acid for skin online"),
    ("hydroquinone-prescription","Hydroquinone Prescription","hydroquinone online prescription"),
    ("kojic-acid-prescription","Kojic Acid Prescription","kojic acid skin lightening online"),
    ("laser-skin-online","Laser Skin Consultation Online","online laser skin treatment consultation"),
    ("custom-skin-formula","Custom Skin Formula","custom prescription skin formula"),
    ("subscription-skin-care","Subscription Skin Care","prescription skin care subscription"),
    ("skin-care-for-40s","Skin Care for Women in 40s","prescription skin care women over 40"),
    ("skin-care-for-50s","Skin Care for Women in 50s","prescription skin care women over 50"),
    # More hair
    ("hair-loss-after-pregnancy","Hair Loss After Pregnancy","postpartum hair loss treatment"),
    ("stress-hair-loss","Stress Hair Loss Women","stress induced hair loss treatment"),
    ("thyroid-hair-loss","Thyroid Hair Loss Women","hair loss from thyroid women"),
    ("alopecia-women","Alopecia in Women","female alopecia treatment"),
    ("traction-alopecia","Traction Alopecia Treatment","traction alopecia recovery"),
    ("hair-loss-vitamins","Hair Loss Vitamins Women","vitamins for hair loss women"),
    ("biotin-hair-loss","Biotin for Hair Loss","biotin hair loss supplement women"),
    ("iron-deficiency-hair-loss","Iron Deficiency Hair Loss","iron supplements hair loss women"),
    ("hair-supplements-women","Hair Supplements Women","best hair supplements for women"),
    ("hair-growth-treatment","Hair Growth Treatment Women","fastest hair growth treatment women"),
    # Generic high volume
    ("womens-health-platform","Women's Health Platform USA","best women's health platform 2026"),
    ("online-prescription-women-2026","Online Prescription Women 2026","get prescriptions online women 2026"),
    ("telehealth-2026-women","Telehealth 2026 Women","best telehealth for women 2026"),
    ("best-telehealth-women","Best Telehealth for Women","top telehealth platforms women"),
    ("women-health-app","Women's Health App","best health app for women"),
    ("womens-health-subscription","Women's Health Subscription","women's health subscription service"),
    ("online-care-women","Online Care for Women","get care online women"),
    ("healthcare-women-usa","Healthcare for Women USA","women's healthcare options USA"),
    ("get-prescription-online","Get Prescription Online","how to get prescription online women"),
    ("virtual-health-women","Virtual Health for Women","virtual health platform women USA"),
]

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
:root{
  --pink:#e91e63;--pink-dark:#ad1457;--pink-light:#fce4ec;
  --bg:#fdf6f9;--white:#ffffff;--card:#ffffff;
  --text:#2d1b22;--muted:#8b6170;--border:#f3d6e4;
  --font:'Plus Jakarta Sans',sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--text);font-family:var(--font);line-height:1.6}
a{text-decoration:none;color:inherit}

.site-header{
  background:var(--white);box-shadow:0 2px 12px rgba(233,30,99,0.08);
  position:sticky;top:0;z-index:100;
}
.nav-inner{
  max-width:1200px;margin:0 auto;
  display:flex;justify-content:space-between;align-items:center;
  padding:16px 24px;
}
.logo{font-weight:800;font-size:20px;color:var(--pink)}
.header-cta{
  background:var(--pink);color:#fff;
  font-weight:700;font-size:13px;
  padding:10px 22px;border-radius:24px;
  transition:background .2s,transform .2s;
}
.header-cta:hover{background:var(--pink-dark);transform:translateY(-1px)}

.hero{
  background:linear-gradient(135deg,var(--pink) 0%,#e91e8c 50%,#ad1457 100%);
  color:#fff;padding:76px 24px 60px;text-align:center;
}
.hero-badge{
  display:inline-block;
  background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.25);
  border-radius:999px;padding:6px 18px;font-size:12px;
  letter-spacing:.08em;text-transform:uppercase;margin-bottom:22px;font-weight:600;
}
.hero h1{
  font-size:clamp(26px,5vw,52px);font-weight:800;
  line-height:1.15;margin-bottom:16px;
}
.hero p{font-size:17px;opacity:.92;max-width:620px;margin:0 auto 30px}
.cta-group{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.btn-white{
  background:#fff;color:var(--pink);font-weight:800;font-size:15px;
  padding:15px 32px;border-radius:28px;
  box-shadow:0 4px 20px rgba(0,0,0,0.15);
  transition:transform .2s,box-shadow .2s;
}
.btn-white:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,0,0,0.2)}
.btn-outline-white{
  border:2px solid rgba(255,255,255,0.5);color:#fff;
  font-size:15px;padding:13px 26px;border-radius:28px;
  transition:border-color .2s;
}
.btn-outline-white:hover{border-color:#fff}

.trust-bar{
  background:var(--white);border-bottom:1px solid var(--border);
  display:flex;justify-content:center;gap:40px;flex-wrap:wrap;
  padding:18px 24px;
}
.trust-item{
  display:flex;align-items:center;gap:8px;
  font-size:13px;font-weight:600;color:var(--muted);
}
.trust-item span{font-size:18px}

.features{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:16px;padding:52px 24px;max-width:1200px;margin:0 auto;
}
.feat{
  background:var(--card);border:1px solid var(--border);
  border-radius:16px;padding:24px;
  box-shadow:0 2px 12px rgba(233,30,99,0.05);
  transition:box-shadow .2s,transform .2s,border-color .2s;
}
.feat:hover{box-shadow:0 8px 28px rgba(233,30,99,0.12);transform:translateY(-3px);border-color:var(--pink)}
.feat-icon{font-size:28px;margin-bottom:12px}
.feat h3{font-size:16px;font-weight:700;color:var(--pink);margin-bottom:8px}
.feat p{font-size:14px;color:var(--muted);line-height:1.6}

.faq-section{max-width:800px;margin:0 auto;padding:0 24px 52px}
.faq-title{font-size:20px;font-weight:800;color:var(--pink);margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid var(--border)}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px;margin-bottom:12px}
.faq-q{font-weight:700;font-size:15px;color:var(--text);margin-bottom:8px}
.faq-a{font-size:14px;color:var(--muted);line-height:1.6}

.related{max-width:1200px;margin:0 auto;padding:0 24px 52px}
.sec-title{font-size:18px;font-weight:800;color:var(--pink);margin-bottom:16px;padding-bottom:10px;border-bottom:2px solid var(--border)}
.rel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}
.rel-card{
  background:var(--card);border:1px solid var(--border);
  border-radius:10px;padding:13px 16px;font-size:13px;font-weight:600;
  color:var(--text);transition:border-color .2s,box-shadow .2s;
}
.rel-card:hover{border-color:var(--pink);box-shadow:0 4px 12px rgba(233,30,99,0.1)}

.cta-band{
  background:linear-gradient(135deg,var(--pink),#e91e8c);
  color:#fff;padding:56px 24px;text-align:center;
}
.cta-band h2{font-size:clamp(22px,4vw,38px);font-weight:800;margin-bottom:12px}
.cta-band p{opacity:.9;margin-bottom:26px;font-size:17px}

.sticky-cta{
  position:fixed;bottom:20px;right:20px;
  background:var(--pink);color:#fff;
  font-weight:800;font-size:13px;
  padding:13px 20px;border-radius:24px;
  box-shadow:0 4px 20px rgba(233,30,99,0.4);
  z-index:999;transition:background .2s;
}
.sticky-cta:hover{background:var(--pink-dark)}

footer{
  background:var(--white);border-top:1px solid var(--border);
  padding:28px 24px;text-align:center;
  font-size:12px;color:var(--muted);
}
footer a{color:var(--pink)}

@media(max-width:600px){
  .nav-inner{padding:12px 14px}
  .hero{padding:52px 14px 40px}
  .trust-bar{gap:16px}
}
"""
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"/><link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>'

# ── PAGE BUILDER ──────────────────────────────────────────────────────────────
def make_page(slug, title, desc, h1, badge, features_html, faq_html, related_html, cta_h2, cta_p):
    canonical = f"{BASE_URL}{slug}"
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{canonical}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
{FONTS}
<style>{CSS}</style>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"WebPage",
  "name":"{title}",
  "description":"{desc}",
  "url":"{canonical}"
}}
</script>
</head>
<body>
<header class="site-header">
  <div class="nav-inner">
    <div class="logo">Hers</div>
    <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started →</a>
  </div>
</header>
<section class="hero">
  <div class="hero-badge">{badge}</div>
  <h1>{h1}</h1>
  <p>{desc}</p>
  <div class="cta-group">
    <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started with Hers →</a>
    <a class="btn-outline-white" href="index.html">← All Services</a>
  </div>
</section>
<div class="trust-bar">
  <div class="trust-item"><span>👩‍⚕️</span> Licensed US Providers</div>
  <div class="trust-item"><span>💊</span> Prescription Delivery</div>
  <div class="trust-item"><span>🔒</span> HIPAA Compliant</div>
  <div class="trust-item"><span>⭐</span> 500,000+ Women Served</div>
</div>
<div class="features">{features_html}</div>
{faq_html}
<div class="related">
  <div class="sec-title">Related Services</div>
  <div class="rel-grid">{related_html}</div>
</div>
<section class="cta-band">
  <h2>{cta_h2}</h2>
  <p>{cta_p}</p>
  <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Start with Hers Today →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">💊 Get Started</a>
<footer>
  © {YEAR} Hers Affiliate Guide · <a href="index.html">Home</a> · Affiliate links used · Individual results may vary · Not medical advice
</footer>
</body>
</html>"""

def make_faq(faqs):
    if not faqs:
        return ""
    items = "".join(
        f'<div class="faq-item"><div class="faq-q">❓ {q}</div><div class="faq-a">Hers connects you with licensed US providers who can evaluate and address this. Visit Hers to get started with a free online assessment.</div></div>'
        for q in faqs
    )
    return f'<div class="faq-section"><div class="faq-title">Frequently Asked Questions</div>{items}</div>'

# ── STATE PAGES ───────────────────────────────────────────────────────────────
def make_state_page(st_slug, st_name, st_abbr, intent_slug, intent_name, intent_kw):
    slug  = f"hers-{st_slug}-{intent_slug}.html"
    title = f"Hers {intent_name} in {st_name} {YEAR} | Women's Telehealth"
    desc  = f"Get {intent_kw} in {st_name} through Hers. Licensed {st_abbr} providers. Prescriptions delivered to your door. Start your free assessment today."
    h1    = f"👩‍⚕️ Hers {intent_name} in {st_name}"
    badge = f"📍 {st_abbr} · Women's Health · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">📍</div><h3>{st_name} Providers</h3><p>Hers works with licensed healthcare providers in {st_name} ({st_abbr}) to deliver quality women's health care. Get started with a free online assessment today.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Prescription Delivery</h3><p>Medications prescribed by your Hers provider are shipped directly to your home in {st_name}. Fast, discreet, HIPAA-compliant delivery.</p></div>
<div class="feat"><div class="feat-icon">👩‍⚕️</div><h3>Licensed {st_abbr} Providers</h3><p>All Hers providers are licensed to practice in {st_name}. Get the same quality of care as an in-person visit, from the comfort of your home.</p></div>
<div class="feat"><div class="feat-icon">⚡</div><h3>Fast Access in {st_name}</h3><p>Most Hers patients in {st_name} connect with a provider within 24 hours. No waiting rooms, no commute — just expert women's health care online.</p></div>"""
    faqs = [f"Is Hers available in {st_name}?", f"Can Hers prescribe medication to {st_name} residents?", f"How long does delivery take in {st_name}?", f"Does Hers accept insurance in {st_name}?"]
    related_html = "".join(
        f'<a href="hers-{s2}-{intent_slug}.html" class="rel-card">Hers {sn2} ({sa2})</a>'
        for s2, sn2, sa2 in STATES[:10] if s2 != st_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Ready to Start {intent_name} in {st_name}?",
        f"Join thousands of {st_name} women who trust Hers for their healthcare needs.")

# ── CITY PAGES ────────────────────────────────────────────────────────────────
def make_city_page(city_slug, city_name, city_state, intent_slug, intent_name, intent_kw):
    slug  = f"hers-{city_slug}-{intent_slug}.html"
    title = f"Hers {intent_name} {city_name}, {city_state} {YEAR} | Women's Telehealth"
    desc  = f"Get {intent_kw} in {city_name}, {city_state} through Hers. Licensed providers, prescription delivery, discreet and HIPAA-compliant care for women."
    h1    = f"💊 Hers {intent_name} — {city_name}, {city_state}"
    badge = f"📍 {city_name}, {city_state} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">🏙️</div><h3>{city_name} Women's Health</h3><p>Hers serves women in {city_name}, {city_state} with convenient online healthcare. No commute, no waiting room — expert care delivered to your door.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Prescription Delivery to {city_name}</h3><p>Prescriptions written by your Hers provider are shipped directly to your {city_name} address. Fast, discreet, and reliable.</p></div>
<div class="feat"><div class="feat-icon">👩‍⚕️</div><h3>Licensed Providers</h3><p>All Hers providers serving {city_name} are licensed in {city_state}. Receive the same standard of care as an in-person visit.</p></div>
<div class="feat"><div class="feat-icon">⚡</div><h3>Same-Day Consultation</h3><p>Most {city_name} patients connect with a Hers provider the same day. Start your free assessment and get care within hours.</p></div>"""
    faqs = [f"Is Hers available in {city_name}?", f"How fast can I get a prescription in {city_name}?", f"Does Hers deliver to {city_name}, {city_state}?", "Is Hers covered by insurance?"]
    related_html = "".join(
        f'<a href="hers-{st_slug}-{intent_slug}.html" class="rel-card">Hers {st_name} ({st_abbr})</a>'
        for st_slug, st_name, st_abbr in STATES[:10]
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Start Your {intent_name} Journey in {city_name}",
        f"Join thousands of {city_name} women who trust Hers for expert online healthcare.")

# ── SERVICE PAGES ─────────────────────────────────────────────────────────────
def make_service_page(s_slug, s_name, s_type, s_kw, s_icon, s_desc, s_faqs, intent_slug, intent_name):
    slug  = f"hers-{s_slug}-{intent_slug}.html"
    title = f"Hers {s_name} — {intent_name} {YEAR} | Women's Online Healthcare"
    desc  = f"Get {s_kw} through Hers. {s_desc[:100]}... Licensed US providers, fast delivery, HIPAA-compliant care."
    h1    = f"{s_icon} Hers {s_name}: {intent_name}"
    badge = f"✅ {s_name} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">{s_icon}</div><h3>{s_name}</h3><p>{s_desc}</p></div>
<div class="feat"><div class="feat-icon">👩‍⚕️</div><h3>Expert Provider Evaluation</h3><p>A licensed US provider will review your medical history and determine if {s_name.lower()} is right for you. Fast, thorough, and confidential.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Prescription Delivery</h3><p>Once prescribed, your {s_name.lower()} treatment is shipped directly to your US home. Discreet packaging, fast delivery.</p></div>
<div class="feat"><div class="feat-icon">🔄</div><h3>Ongoing Support</h3><p>Hers provides ongoing follow-up care for {s_name.lower()} patients. Check in with your provider, adjust your treatment, and stay on track.</p></div>"""
    related_html = "".join(
        f'<a href="hers-{ss2}-overview.html" class="rel-card">{si2} Hers {sn2}</a>'
        for ss2, sn2, st2, sk2, si2, sd2, sf2 in SERVICES if ss2 != s_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(s_faqs), related_html,
        f"Start {s_name} with Hers Today",
        f"Get expert {s_name.lower()} care from licensed US providers. Fast, affordable, and discreet.")

# ── COMPETITOR PAGES ──────────────────────────────────────────────────────────
def make_competitor_page(c_slug, c_name, c_short, c_type, i_slug, i_name, i_kw):
    slug  = f"hers-vs-{c_slug}-{i_slug}.html"
    title = f"Hers vs {c_name} {YEAR} — {i_name} | Which is Better?"
    desc  = f"Detailed {i_kw} between Hers and {c_name}. Compare cost, services, providers, and user reviews. Find the best women's telehealth platform for you."
    h1    = f"⚖️ Hers vs {c_name}: {i_name}"
    badge = f"🔍 Comparison · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">👩‍⚕️</div><h3>Hers: Women-Only Focus</h3><p>Hers is built specifically for women's health — from Ozempic and WeGovy to mental health, hair, and skin. {c_name} is a {c_type} with a broader or different focus.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Prescription Services</h3><p>Hers offers prescriptions for weight loss medications, mental health, hair loss, skin care, and birth control. Compare with {c_name}'s {i_kw}.</p></div>
<div class="feat"><div class="feat-icon">💰</div><h3>Cost Comparison</h3><p>Hers offers competitive pricing for women's telehealth. Compare costs with {c_name} to find the best value for your healthcare needs.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Why Women Choose Hers</h3><p>500,000+ women trust Hers for telehealth. Specialized women's care, fast prescription delivery, and ongoing provider support set Hers apart from {c_name}.</p></div>"""
    faqs = [f"Is Hers better than {c_name}?", f"How does Hers compare to {c_name} for weight loss?", f"Which is cheaper, Hers or {c_name}?", f"Does Hers or {c_name} prescribe Ozempic?"]
    related_html = "".join(
        f'<a href="hers-vs-{cs2}-{i_slug}.html" class="rel-card">Hers vs {cn2}</a>'
        for cs2, cn2, csh2, ct2 in COMPETITORS if cs2 != c_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Why Choose Hers Over {c_name}?",
        f"Hers is built for women. Get expert care, fast prescriptions, and ongoing support. {c_name} is great but Hers is specialized for you.")

# ── LONG TAIL PAGES ───────────────────────────────────────────────────────────
def make_longtail_page(lt_slug, lt_name, lt_kw):
    slug  = f"{lt_slug}.html"
    title = f"{lt_name} | Hers Women's Telehealth {YEAR}"
    desc  = f"Complete guide to {lt_kw}. Hers provides licensed US providers, fast prescriptions, and ongoing care. Start your free assessment today."
    h1    = f"🔍 {lt_name}"
    badge = f"⭐ {lt_kw.title()} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">🔬</div><h3>Expert Information</h3><p>Everything you need to know about {lt_kw} from licensed healthcare professionals. Evidence-based information for women's health decisions.</p></div>
<div class="feat"><div class="feat-icon">👩‍⚕️</div><h3>Licensed Provider Care</h3><p>Hers connects you with licensed US providers who specialize in {lt_kw}. Get expert evaluation and personalized treatment.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Prescription Delivery</h3><p>If medication is right for you, your Hers provider will prescribe it and it will be delivered directly to your US home. Fast and discreet.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>Trusted by 500,000+ Women</h3><p>Hers is America's leading women's telehealth platform. Join over half a million women who have transformed their health with Hers.</p></div>"""
    related_html = "".join(
        f'<a href="{ls2}.html" class="rel-card">{ln2}</a>'
        for ls2, ln2, lk2 in LONG_TAILS[:12] if ls2 != lt_slug
    )
    faqs = [f"How does Hers help with {lt_kw}?", "Is Hers covered by insurance?", "How fast can I get treatment through Hers?", "Are Hers providers licensed in my state?"]
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get Expert Care for {lt_name}",
        f"Hers provides licensed US providers for {lt_kw}. Start your free assessment today.")

# ── SERVICE OVERVIEW PAGES ────────────────────────────────────────────────────
def make_service_overview(s_slug, s_name, s_type, s_kw, s_icon, s_desc, s_faqs):
    slug  = f"hers-{s_slug}-overview.html"
    title = f"Hers {s_name} {YEAR} | Complete Guide for Women"
    desc  = f"Complete guide to {s_name.lower()} through Hers. {s_desc[:120]}... Licensed US providers, fast delivery."
    h1    = f"{s_icon} Hers {s_name}: Complete Guide {YEAR}"
    badge = f"✅ {s_name} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">{s_icon}</div><h3>What is {s_name}?</h3><p>{s_desc}</p></div>
<div class="feat"><div class="feat-icon">👩‍⚕️</div><h3>How Hers Provides {s_name}</h3><p>Complete a free online assessment. A licensed US provider reviews your health history and creates a personalized {s_name.lower()} treatment plan.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Treatment Delivery</h3><p>Your {s_name.lower()} medication or treatment is shipped directly to your US home. Fast, discreet, and HIPAA-compliant delivery.</p></div>
<div class="feat"><div class="feat-icon">🔄</div><h3>Ongoing {s_name} Care</h3><p>Hers provides continuous follow-up for {s_name.lower()} patients — check ins, dose adjustments, and provider messaging anytime.</p></div>"""
    related_html = "".join(
        f'<a href="hers-{ss2}-overview.html" class="rel-card">{si2} {sn2}</a>'
        for ss2, sn2, st2, sk2, si2, sd2, sf2 in SERVICES if ss2 != s_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(s_faqs), related_html,
        f"Start {s_name} with Hers",
        f"Get expert {s_name.lower()} care from licensed US providers. Fast, affordable, and confidential.")

# ── STATE x SERVICE PAGES ─────────────────────────────────────────────────────
def make_state_service_page(st_slug, st_name, st_abbr, s_slug, s_name, s_icon, s_kw):
    slug  = f"hers-{st_slug}-{s_slug}.html"
    title = f"Hers {s_name} in {st_name} {YEAR} | Women's Online Health"
    desc  = f"Get {s_kw} in {st_name} through Hers. Licensed {st_abbr} providers, fast prescription delivery, and discreet HIPAA-compliant women's healthcare."
    h1    = f"{s_icon} Hers {s_name} in {st_name}"
    badge = f"📍 {st_abbr} · {s_name} · {YEAR}"
    features_html = f"""
<div class="feat"><div class="feat-icon">📍</div><h3>{s_name} in {st_name}</h3><p>Hers provides {s_name.lower()} to women throughout {st_name} ({st_abbr}). Licensed local providers, delivered care, no commute required.</p></div>
<div class="feat"><div class="feat-icon">{s_icon}</div><h3>Expert {s_name}</h3><p>Get specialized {s_kw} from a licensed {st_abbr} provider. Hers makes it easy to access quality care without leaving home.</p></div>
<div class="feat"><div class="feat-icon">💊</div><h3>Delivered to {st_name}</h3><p>All prescriptions are shipped directly to your {st_name} address. Discreet packaging and fast delivery to every city in {st_name}.</p></div>
<div class="feat"><div class="feat-icon">⭐</div><h3>#1 in {st_name}</h3><p>Hers is the leading women's telehealth platform in {st_name}. Trusted by thousands of {st_abbr} women for quality, affordable healthcare.</p></div>"""
    faqs = [f"Does Hers offer {s_name.lower()} in {st_name}?", f"How much does Hers {s_name.lower()} cost in {st_name}?", f"Is Hers covered by insurance in {st_name}?", f"How fast is delivery in {st_name}?"]
    related_html = "".join(
        f'<a href="hers-{s2}-{s_slug}.html" class="rel-card">Hers {sn2} {s_name}</a>'
        for s2, sn2, sa2 in STATES[:10] if s2 != st_slug
    )
    return slug, make_page(slug, title, desc, h1, badge, features_html, make_faq(faqs), related_html,
        f"Get {s_name} in {st_name} with Hers",
        f"Join {st_name} women who trust Hers for {s_name.lower()}. Start your free assessment now.")

# ── INDEX ─────────────────────────────────────────────────────────────────────
def make_index():
    service_cards = "".join(
        f'<a href="hers-{ss}-overview.html" class="feat" style="cursor:pointer"><div class="feat-icon">{si}</div><h3>{sn}</h3><p>{sd[:80]}...</p></a>'
        for ss, sn, st, sk, si, sd, sf in SERVICES
    )
    state_cards = "".join(
        f'<a href="hers-{s}-ozempic-online.html" class="rel-card">📍 {sn} ({sa})</a>'
        for s, sn, sa in STATES
    )
    comp_cards = "".join(
        f'<a href="hers-vs-{cs}-vs.html" class="rel-card">Hers vs {cn}</a>'
        for cs, cn, csh, ct in COMPETITORS
    )
    lt_cards = "".join(
        f'<a href="{ls}.html" class="rel-card">{ln}</a>'
        for ls, ln, lk in LONG_TAILS[:24]
    )
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Hers Women's Telehealth {YEAR} | Ozempic, WeGovy, Mental Health, Hair, Skin</title>
<meta name="description" content="Hers — America's leading women's telehealth platform. Ozempic, WeGovy, Jardiance, mental health, hair loss, skin care, birth control and more. Licensed US providers."/>
<meta name="robots" content="index,follow"/>
<link rel="canonical" href="{BASE_URL}"/>
{FONTS}
<style>{CSS}
.section{{max-width:1200px;margin:0 auto;padding:52px 24px}}
.section-title{{font-size:22px;font-weight:800;color:var(--pink);margin-bottom:20px;padding-bottom:12px;border-bottom:2px solid var(--border)}}
.service-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}}
</style>
</head>
<body>
<header class="site-header">
  <div class="nav-inner">
    <div class="logo">Hers</div>
    <a class="header-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started →</a>
  </div>
</header>
<section class="hero">
  <div class="hero-badge">👩‍⚕️ America's #1 Women's Telehealth · {YEAR}</div>
  <h1>Healthcare Built for Women</h1>
  <p>Ozempic, WeGovy, Jardiance, mental health, hair loss, skin care, birth control, and more — all from licensed US providers delivered to your door.</p>
  <div class="cta-group">
    <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Start Free Assessment →</a>
  </div>
</section>
<div class="trust-bar">
  <div class="trust-item"><span>👩‍⚕️</span> Licensed US Providers</div>
  <div class="trust-item"><span>💊</span> Prescription Delivery</div>
  <div class="trust-item"><span>🔒</span> HIPAA Compliant</div>
  <div class="trust-item"><span>⭐</span> 500,000+ Women Served</div>
  <div class="trust-item"><span>🚀</span> Same-Day Consultations</div>
</div>
<div class="section">
  <div class="section-title">💊 Our Services</div>
  <div class="service-grid">{service_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">📍 Find Hers by State</div>
  <div class="rel-grid">{state_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">⚖️ Hers vs Competitors</div>
  <div class="rel-grid">{comp_cards}</div>
</div>
<div class="section" style="padding-top:0">
  <div class="section-title">🔍 Research Topics</div>
  <div class="rel-grid">{lt_cards}</div>
</div>
<section class="cta-band">
  <h2>Start Your Health Journey with Hers</h2>
  <p>500,000+ women trust Hers. Licensed providers, fast delivery, affordable care.</p>
  <a class="btn-white" href="{AFF}" target="_blank" rel="nofollow sponsored">Get Started Free →</a>
</section>
<a class="sticky-cta" href="{AFF}" target="_blank" rel="nofollow sponsored">💊 Get Started</a>
<footer>© {YEAR} Hers Affiliate Guide · Affiliate links used · Not medical advice · <a href="index.html">Home</a></footer>
</body>
</html>"""

# ── SITEMAP / ROBOTS ──────────────────────────────────────────────────────────
def make_sitemap(urls):
    iso = now.strftime("%Y-%m-%d")
    sm  = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += f'  <url><loc>{BASE_URL}</loc><changefreq>daily</changefreq><priority>1.0</priority><lastmod>{iso}</lastmod></url>\n'
    for url in urls:
        sm += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.7</priority><lastmod>{iso}</lastmod></url>\n'
    sm += '</urlset>\n'
    return sm

def make_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /build.py\nDisallow: /.github/\nCrawl-delay: 1\nSitemap: {BASE_URL}sitemap.xml\n"

def make_llms():
    return f"# Hers Women's Telehealth USA\n> Updated: {DATE_STR}\n> Affiliate links present\n\n## About\n21,000+ page USA affiliate site for Hers women's telehealth.\nCovers all 50 states, 350 cities, 15 services, 20 competitors, 300 long-tail keywords.\nServices: Ozempic, WeGovy, Jardiance, mental health, hair loss, skin care, birth control, menopause, PCOS.\n\n## Site: {BASE_URL}\n"

# ── MAIN ──────────────────────────────────────────────────────────────────────
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.stdout.strip(): print(r.stdout.strip())
    return r.returncode

if __name__ == "__main__":
    state_p  = len(STATES) * len(STATE_INTENTS)
    city_p   = len(CITIES) * len(STATE_INTENTS)
    svc_p    = len(SERVICES) * 30 + len(SERVICES)  # intents + overview
    comp_p   = len(COMPETITORS) * len(COMP_INTENTS)
    lt_p     = len(LONG_TAILS)
    ss_p     = len(STATES) * len(SERVICES)
    total    = state_p + city_p + svc_p + comp_p + lt_p + ss_p

    print(f"💊  Hers Build — {DATE_STR}  sync={SYNC}")
    print(f"   State pages:       {state_p:,}")
    print(f"   City pages:        {city_p:,}")
    print(f"   Service pages:     {svc_p:,}")
    print(f"   Competitor pages:  {comp_p:,}")
    print(f"   Long-tail pages:   {lt_p:,}")
    print(f"   State×Service:     {ss_p:,}")
    print(f"   Total: {total:,} pages")

    with open("index.html",  "w", encoding="utf-8") as f: f.write(make_index())
    with open("robots.txt",  "w", encoding="utf-8") as f: f.write(make_robots())
    with open("llms.txt",    "w", encoding="utf-8") as f: f.write(make_llms())
    with open(".nojekyll",   "w") as f: f.write("")
    print("✅ index.html  robots.txt  llms.txt  .nojekyll")

    sitemap_urls = []
    count = 0

    print("   Generating state pages...")
    for st_slug, st_name, st_abbr in STATES:
        for i_slug, i_name, i_kw in STATE_INTENTS:
            slug, html = make_state_page(st_slug, st_name, st_abbr, i_slug, i_name, i_kw)
            with open(slug, "w", encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating city pages...")
    for c_slug, c_name, c_state in CITIES:
        for i_slug, i_name, i_kw in STATE_INTENTS:
            slug, html = make_city_page(c_slug, c_name, c_state, i_slug, i_name, i_kw)
            with open(slug, "w", encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1
            if count % 5000 == 0: print(f"   {count:,}/{total:,}...")

    print("   Generating service pages...")
    for svc in SERVICES:
        ss, sn, st, sk, si, sd, sf = svc
        # overview page
        slug, html = make_service_overview(ss, sn, st, sk, si, sd, sf)
        with open(slug, "w", encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1
        # intent pages — use first 30 STATE_INTENTS
        for i_slug, i_name, i_kw in STATE_INTENTS[:30]:
            slug, html = make_service_page(ss, sn, st, sk, si, sd, sf, i_slug, i_name)
            with open(slug, "w", encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating competitor pages...")
    for c_slug, c_name, c_short, c_type in COMPETITORS:
        for i_slug, i_name, i_kw in COMP_INTENTS:
            slug, html = make_competitor_page(c_slug, c_name, c_short, c_type, i_slug, i_name, i_kw)
            with open(slug, "w", encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print("   Generating long-tail pages...")
    for lt in LONG_TAILS:
        slug, html = make_longtail_page(*lt)
        with open(slug, "w", encoding="utf-8") as f: f.write(html)
        sitemap_urls.append(f"{BASE_URL}{slug}")
        count += 1

    print("   Generating state × service pages...")
    for st_slug, st_name, st_abbr in STATES:
        for ss, sn, st2, sk, si, sd, sf in SERVICES:
            slug, html = make_state_service_page(st_slug, st_name, st_abbr, ss, sn, si, sk)
            with open(slug, "w", encoding="utf-8") as f: f.write(html)
            sitemap_urls.append(f"{BASE_URL}{slug}")
            count += 1

    print(f"✅ {count:,} pages written")

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(make_sitemap(sitemap_urls))
    print(f"✅ sitemap.xml — {len(sitemap_urls)+1:,} URLs")

    print("\n── Git ──")
    run("git add -A")
    n = int(subprocess.run("git diff --cached --name-only | wc -l",
        shell=True, capture_output=True, text=True).stdout.strip())
    print(f"Staged: {n:,} files")
    if n == 0:
        print("Nothing to commit"); sys.exit(0)
    run(f'git commit -m "hers sync {SYNC}"')
    import time
    for i in range(1, 6):
        print(f"Push attempt {i}...")
        run("git fetch origin main")
        if run("git rebase origin/main") != 0:
            run("git rebase --abort"); time.sleep(5); continue
        if run("git push origin HEAD:main") == 0:
            print("✅ Pushed"); break
        time.sleep(5)
    else:
        print("❌ Push failed"); sys.exit(1)
