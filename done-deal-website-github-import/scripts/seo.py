"""Canonical, social, and structured metadata for the published static pages."""

from html import escape
from json import dumps
from xml.etree.ElementTree import Element, SubElement, tostring

# This is the only hostname attached to the production Pages project.
# Update this origin when a custom domain is confirmed live.
ORIGIN = "https://done-deal-website.pages.dev"
NAME = "Done Deal Auto Group"
CARD_PATH = "/assets/done-deal-share.jpg"
CARD_ALT = "Done Deal Auto Group’s D-road logo beside a blue road motif on a navy background."
HOME_TITLE = "Done Deal Auto Group | Car Buying & Leasing Help"
HOME_DESCRIPTION = (
    "Done Deal Auto Group helps you find the right car, compare buying and "
    "leasing options, and request a quote."
)

# Search title, search description, short share title, and breadcrumb label.
METADATA = {
    "/": (HOME_TITLE, HOME_DESCRIPTION, "A better car shopping experience", "Home"),
    "/services/": ("Car Buying, Leasing & Trade-In Help", "Get help buying or leasing a new car, evaluating a trade-in, or planning a lease return. Done Deal explains the options and helps negotiate the offer.", "Car buying and leasing help", "Services"),
    "/about/": ("About Done Deal Auto Group", "Learn how Done Deal Auto Group helps customers search for a vehicle, compare offers, and negotiate the details before making a decision.", "Meet Done Deal Auto Group", "About"),
    "/contact/": ("Contact Done Deal Auto Group", "Call, text, or email Done Deal Auto Group in Deer Park, New York, with questions about buying, leasing, trading in, or returning a vehicle.", "Talk to Done Deal Auto Group", "Contact"),
    "/request-a-quote/": ("Request a Car Quote", "Tell Done Deal Auto Group what you’re looking for, your budget, and your timing. Request a quote without committing to a purchase.", "Request a car quote", "Request a Quote"),
    "/customer-stories/": ("Customer Stories", "See how Done Deal helped Ed, Liz, Joanne, and Christina compare offers, move out of leases, trade in vehicles, and find their next cars.", "Real customers. Better deals.", "Customer Stories"),
    "/customer-stories/california/": ("Christina’s Mercedes-Benz GLS 450 Story", "See how Done Deal helped Christina save on a 2026 Mercedes-Benz GLS 450 in California and end her existing lease early without additional charges.", "Christina’s new Mercedes-Benz", "Christina"),
    "/customer-stories/virginia/": ("Ed’s Toyota Sienna Story", "See how Done Deal helped Ed end his lease early and move into a Toyota Sienna, with home delivery and driveway pickup in Virginia.", "Ed’s Toyota Sienna, delivered", "Ed"),
    "/customer-stories/liz/": ("Liz’s Acura MDX Lease Story", "See how Done Deal matched Liz’s trade-in offer and helped her lease a new Acura MDX after her previous car passed 100,000 miles.", "Liz’s new Acura MDX", "Liz"),
    "/customer-stories/joanne/": ("Joanne’s Car Shopping Story", "See how Done Deal helped Joanne find a better price after several dealership visits and saved her days of additional car shopping research.", "How Joanne found a better price", "Joanne"),
}


def meta(key, value, attribute="name"):
    return f'<meta {attribute}="{key}" content="{escape(value, quote=True)}">'


def structured_data(path, label):
    org_id = ORIGIN + "/#organization"
    if path == "/":
        return {
            "@context": "https://schema.org", "@type": "Organization",
            "@id": org_id, "name": NAME, "url": ORIGIN + "/",
            "logo": ORIGIN + "/assets/logo.png",
            "telephone": "+1-631-525-7010", "email": "info@donedealautogroup.com",
            "address": {"@type": "PostalAddress", "streetAddress": "10 Burt Drive",
                        "addressLocality": "Deer Park", "addressRegion": "NY",
                        "postalCode": "11729", "addressCountry": "US"},
        }
    trail = [("Home", "/")]
    if path.startswith("/customer-stories/") and path != "/customer-stories/":
        trail.append(("Customer Stories", "/customer-stories/"))
    trail.append((label, path))
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": ORIGIN + url}
            for i, (name, url) in enumerate(trail, 1)
        ],
    }


def render_seo(path, title, description, draft):
    tags = []
    if draft:
        tags.append(meta("robots", "noindex,nofollow"))
    else:
        title, description, share_title, label = METADATA[path]
        if path not in ("/", "/about/", "/contact/"):
            title += " | " + NAME
    if draft:
        title += " | " + NAME
    tags[:0] = [f"<title>{escape(title)}</title>", meta("description", description)]
    tags += [
        '<link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">',
        '<link rel="icon" type="image/png" href="/favicon.png" sizes="96x96">',
        '<link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">',
    ]
    if draft:
        return "\n".join(tags)

    url = ORIGIN + path
    card = ORIGIN + CARD_PATH
    share_description = (
        "Get help finding the right car, comparing your options, and getting a quote."
        if path == "/" else description
    )
    tags += [
        f'<link rel="canonical" href="{url}">',
        *(meta("og:" + key, value, "property") for key, value in {
            "title": share_title, "description": share_description,
            "site_name": NAME, "type": "website", "url": url, "image": card,
            "image:type": "image/jpeg", "image:width": "1200", "image:height": "630",
            "image:alt": CARD_ALT,
        }.items()),
        *(meta("twitter:" + key, value) for key, value in {
            "card": "summary_large_image", "title": share_title,
            "description": share_description, "image": card, "image:alt": CARD_ALT,
        }.items()),
        '<script type="application/ld+json">'
        + dumps(structured_data(path, label), ensure_ascii=False).replace("<", "\\u003c")
        + "</script>",
    ]
    return "\n".join(tags)


def render_sitemap(paths):
    sitemap = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for path in paths:
        SubElement(SubElement(sitemap, "url"), "loc").text = ORIGIN + path
    return tostring(sitemap, encoding="unicode", xml_declaration=True) + "\n"
