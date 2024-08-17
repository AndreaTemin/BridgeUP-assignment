# app/data.py

from app.models import Source, Category, Campaign

data = {
    "source-a": Source(w=0).model_dump(),
    "source-b": Source(
        w=100,
        categories={
            "kitchen-tools": Category(
                w=20,
                campaigns={
                    "electric-garlic-chopper": Campaign(w=100).model_dump()
                }
            ).model_dump(),
            "gadgets": Category(
                w=50,
                campaigns={
                    "smartphone-stand": Campaign(w=20).model_dump(),
                    "wireless-charger": Campaign(w=50).model_dump(),
                    "wireless-gadget-01": Campaign(w=30).model_dump(),
                }
            ).model_dump(),
        }
    ).model_dump()
}
