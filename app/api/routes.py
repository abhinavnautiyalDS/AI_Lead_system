from fastapi import APIRouter, HTTPException
from app.schemas.lead_schema import LeadRequest
from app.services.classifier import classify_lead
from app.services.responder import generate_response
from app.database.db import SessionLocal
from app.database.models import Lead

router = APIRouter()

@router.post("/process-lead")
def process_lead(data: LeadRequest):

    if not data.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    try:

        category = classify_lead(data.message)

        response = generate_response(
            data.message,
            category
        )

        db = SessionLocal()

        new_lead = Lead(
            message=data.message,
            category=category,
            response=response,
            status="success"
        )

        db.add(new_lead)
        db.commit()
        db.close()

        return {
            "category": category,
            "response": response,
            "status": "success"
        }

    except Exception as e:

        return {
            "category": "general",
            "response": "Thank you for contacting us. Our team will reach out shortly.",
            "status": "fallback",
            "error": str(e)
        }