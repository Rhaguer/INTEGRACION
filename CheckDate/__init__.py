import datetime
import azure.functions as func
import json

feriados = ["2025-10-12", "2025-10-31", "2025-11-01", "2025-11-16", "2025-12-08"]

def main(req: func.HttpRequest) -> func.HttpResponse:
    fecha_str = req.params.get('date')
    if not fecha_str:
        return func.HttpResponse("Falta parámetro date", status_code=400)
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        return func.HttpResponse("Formato de fecha inválido", status_code=400)

    es_feriado = fecha.weekday() >= 5 or fecha_str in feriados
    return func.HttpResponse(json.dumps(es_feriado), mimetype="application/json")