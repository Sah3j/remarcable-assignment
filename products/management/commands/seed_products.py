from django.core.management.base import BaseCommand
from products.models import Product, Category, Tag


class Command(BaseCommand):
    help = "Seed the database with sample construction-material data (categories, tags, products)"

    def handle(self, *args, **options):
        # --- Categories ---
        category_names = [
            "Conduit & Fittings",
            "Cable & Wire",
            "Boxes & Enclosures",
            "Tools",
            "Safety Equipment",
        ]
        for name in category_names:
            Category.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS(f"Categories ready: {len(category_names)}"))

        # --- Tags ---
        tag_names = [
            "Steel", "PVC", "Galvanized", "Weatherproof", "Indoor",
            "Outdoor", "Heavy-Duty", "Fire-Rated", "Compression", "Threaded",
        ]
        for name in tag_names:
            Tag.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS(f"Tags ready: {len(tag_names)}"))

        # --- Products ---
        products = [
            # Conduit & Fittings
            {
                "name": '3/4" EMT Conduit – 10FT',
                "description": "Electrical metallic tubing for protecting and routing electrical wiring in exposed indoor runs. Lightweight and easy to bend.",
                "category": "Conduit & Fittings",
                "tags": ["Steel", "Indoor"],
            },
            {
                "name": '1/2" Rigid Steel Conduit',
                "description": "Heavy-wall galvanized steel conduit for maximum physical protection of conductors in demanding environments.",
                "category": "Conduit & Fittings",
                "tags": ["Steel", "Galvanized", "Threaded", "Heavy-Duty", "Outdoor"],
            },
            {
                "name": '3/4" EMT Compression Connector',
                "description": "Steel compression fitting for joining EMT conduit to boxes with a secure, watertight connection.",
                "category": "Conduit & Fittings",
                "tags": ["Steel", "Compression", "Weatherproof"],
            },
            {
                "name": "90° Conduit Elbow, Steel",
                "description": "Prefabricated 90-degree sweep for changing conduit direction without field bending.",
                "category": "Conduit & Fittings",
                "tags": ["Steel", "Threaded"],
            },
            {
                "name": '1" PVC Conduit – 10FT',
                "description": "Schedule 40 non-metallic conduit for underground and corrosion-prone outdoor installations.",
                "category": "Conduit & Fittings",
                "tags": ["PVC", "Outdoor", "Weatherproof"],
            },
            # Cable & Wire
            {
                "name": "12 AWG THHN Wire – 500FT",
                "description": "Single-conductor building wire rated for use in conduit and raceways, heat and moisture resistant.",
                "category": "Cable & Wire",
                "tags": ["Indoor", "Heavy-Duty"],
            },
            {
                "name": "14/2 Romex Cable – 250FT",
                "description": "Non-metallic sheathed cable for residential branch circuits, includes ground conductor.",
                "category": "Cable & Wire",
                "tags": ["Indoor"],
            },
            {
                "name": "CAT6 Ethernet Cable – 1000FT",
                "description": "Bulk data cable for high-speed network installations in commercial buildings.",
                "category": "Cable & Wire",
                "tags": ["Indoor"],
            },
            {
                "name": "Bare Copper Grounding Wire – 100FT",
                "description": "Solid bare copper conductor for electrical grounding and bonding applications.",
                "category": "Cable & Wire",
                "tags": ["Outdoor", "Heavy-Duty"],
            },
            {
                "name": "Fire-Rated Alarm Cable – 500FT",
                "description": "Shielded plenum cable for fire alarm and life-safety systems, meets fire-rating codes.",
                "category": "Cable & Wire",
                "tags": ["Fire-Rated", "Indoor"],
            },
            # Boxes & Enclosures
            {
                "name": '4" Square Junction Box, Steel',
                "description": "Galvanized steel electrical box for splicing and routing conductors in indoor installations.",
                "category": "Boxes & Enclosures",
                "tags": ["Steel", "Galvanized", "Indoor"],
            },
            {
                "name": "Single-Gang Weatherproof Box",
                "description": "Die-cast metal outlet box with gasketed cover for outdoor and wet-location use.",
                "category": "Boxes & Enclosures",
                "tags": ["Weatherproof", "Outdoor", "Steel"],
            },
            {
                "name": "NEMA 3R Enclosure, 12x12",
                "description": "Rainproof steel enclosure for housing electrical equipment in outdoor environments.",
                "category": "Boxes & Enclosures",
                "tags": ["Steel", "Weatherproof", "Outdoor", "Heavy-Duty"],
            },
            {
                "name": "PVC Outlet Box, Outdoor",
                "description": "Corrosion-resistant non-metallic box for exposed outdoor electrical devices.",
                "category": "Boxes & Enclosures",
                "tags": ["PVC", "Outdoor", "Weatherproof"],
            },
            {
                "name": "Fire-Rated Access Panel, 12x12",
                "description": "Rated wall/ceiling access door for maintaining fire-barrier integrity around utilities.",
                "category": "Boxes & Enclosures",
                "tags": ["Fire-Rated", "Steel", "Indoor"],
            },
            # Tools
            {
                "name": 'Conduit Bender, 1/2"–3/4"',
                "description": "Hand bender with cast aluminum head for accurate field bends in EMT conduit.",
                "category": "Tools",
                "tags": ["Heavy-Duty", "Steel"],
            },
            {
                "name": "Wire Stripper / Cutter",
                "description": "Insulated hand tool for stripping and cutting common wire gauges cleanly.",
                "category": "Tools",
                "tags": ["Indoor"],
            },
            {
                "name": "Cordless Impact Driver",
                "description": "High-torque battery-powered driver for fast fastening in demanding job-site conditions.",
                "category": "Tools",
                "tags": ["Heavy-Duty"],
            },
            {
                "name": "Fish Tape – 100FT",
                "description": "Steel pulling tape for routing conductors through conduit and wall cavities.",
                "category": "Tools",
                "tags": ["Steel", "Heavy-Duty"],
            },
            # Safety Equipment
            {
                "name": "Hard Hat, Class E",
                "description": "Electrical-rated hard hat protecting against impact and high-voltage contact up to 20,000V.",
                "category": "Safety Equipment",
                "tags": ["Heavy-Duty", "Outdoor"],
            },
            {
                "name": "Safety Glasses, Anti-Fog",
                "description": "Impact-resistant protective eyewear with anti-fog coating for all-day job-site wear.",
                "category": "Safety Equipment",
                "tags": ["Indoor", "Outdoor"],
            },
            {
                "name": "Insulated Work Gloves, 1000V",
                "description": "Rubber insulating gloves rated for live electrical work up to 1000 volts.",
                "category": "Safety Equipment",
                "tags": ["Heavy-Duty", "Weatherproof"],
            },
        ]

        created_count = 0
        for item in products:
            category = Category.objects.get(name=item["category"])
            product, created = Product.objects.get_or_create(
                name=item["name"],
                defaults={
                    "description": item["description"],
                    "category": category,
                },
            )
            product.tags.set(Tag.objects.filter(name__in=item["tags"]))

            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {product.name}"))
            else:
                self.stdout.write(f"Exists (skipped): {product.name}")

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created_count} new products created, {len(products)} total processed."
        ))