# complementos-telematica

**Autor:** Juan Vicente Campos Maciá

## Qué hace el script

`red.py` pide una dirección IPv4 con máscara en formato CIDR (por ejemplo `192.168.1.10/24`) y muestra la dirección de red, la dirección de broadcast, el número de hosts disponibles y la primera y la última IP usable. Si la entrada no es válida, muestra un mensaje de error.

## Cómo se ejecuta

```
python red.py
```

Ejemplo:

```
Introduce una dirección IPv4 con máscara CIDR: 192.168.1.10/24
Dirección de red: 192.168.1.0
Dirección de broadcast: 192.168.1.255
Hosts disponibles: 254
Primera IP usable: 192.168.1.1
Última IP usable: 192.168.1.254
```

## Cómo lo hice con Copilot

**Prompt que usé en el chat de Copilot (VS Code):**

> Escribe un script en Python que pida al usuario una dirección IP con máscara en formato CIDR (por ejemplo 192.168.1.10/24) y muestre la dirección de red, la dirección de broadcast y el número de hosts disponibles. Explícame brevemente cómo funciona.

**Pregunta que le hice después:** ¿Por qué hay que restar 2 a los hosts si el prefijo es 30 o menor, y qué pasa con /31 y /32? Me explicó que la dirección de red y la de broadcast no se pueden asignar a equipos, y que en /31 hay 2 hosts utilizables y en /32 uno.

**Qué cambié yo:** añadí a mano las líneas que muestran la primera y la última IP usable (solo para prefijos /30 o menores, porque en /31 y /32 no hay dirección de red ni de broadcast reservadas).
