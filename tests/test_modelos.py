import pytest
from pydantic import ValidationError

from practica.modelos import EstadoTicket, Orden, Producto, Reserva, Ticket, Usuario


def test_usuario_valido():
    u = Usuario(nombre="Ovidio", email="ovidio@ejemplo.com", edad=30)
    assert u.edad == 30


def test_usuario_email_invalido():
    with pytest.raises(ValidationError):
        Usuario(nombre="Ovidio", email="esto-no-es-un-email", edad=30)


###


def test_producto_valido():
    p = Producto(nombre="Test", precio="10.567", descuento_pct=10)
    assert p.precio == 10.57


def test_producto_precio_invalido():
    with pytest.raises(ValidationError):
        Producto(nombre="Producto123", precio=0, descuento_pct=100)


def test_producto_descuento_fuera_de_rango():
    with pytest.raises(ValidationError):
        Producto(nombre="Producto123", precio=845067.1545, descuento_pct=350)


###


def test_orden_valida():
    o = Orden(
        id_orden="00001",
        productos=[Producto(nombre="Producto1", precio=120.50, descuento_pct=10)],
    )
    assert o.total == 108.45


def test_orden_precioinvalido():
    with pytest.raises(ValidationError):
        Orden(
            id_orden="00001",
            productos=[
                {"nombre": "Producto1", "precio": 1500, "descuento_pct": 10},
                {"nombre": "Producto2", "precio": -250, "descuento_pct": 5},
                {"nombre": "Producto3", "precio": 100, "descuento_pct": 75},
            ],
        )


###


def test_ticket_valido():
    t = Ticket(titulo="Ticket01", estado=EstadoTicket.EN_PROGRESO)
    assert t.estado == "en_progreso"


def test_ticket_invalido():
    with pytest.raises(ValidationError):
        Ticket(titulo="Ticket01", estado="pendiente")


def test_ticket_default():
    t = Ticket(titulo="Ticket03")
    assert t.estado == "abierto"


###


def test_reserva_valida():
    r = Reserva(fecha_inicio="2026-11-30", fecha_fin="2026-12-31", huespedes="3")
    assert r.huespedes == 3
    t2 = Ticket(titulo="Ticket02")
    assert t2.estado == "abierto"


def test_reserva_invalida():
    with pytest.raises(ValidationError):
        Reserva(fecha_inicio="2026-12-31", fecha_fin="2026-11-30", huespedes="5")


def test_noches_validas():
    r = Reserva(fecha_inicio="2026-09-01", fecha_fin="2026-09-08", huespedes="10")
    assert r.noches == 7
