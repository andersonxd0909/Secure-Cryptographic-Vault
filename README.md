# 🎭 Fake Identity & Temp-Mail Generator

Este es un proyecto de **software de privacidad** desarrollado en Python. Su función es generar identidades falsas completas (nombres, direcciones, etc.) y proporcionar correos electrónicos temporales de 10 minutos con contraseñas seguras para proteger la identidad real del usuario en internet.

> [!CAUTION]
> **AVISO LEGAL:** Esta herramienta fue creada con fines educativos y para proteger la privacidad del usuario frente al spam. No debe utilizarse para actividades ilícitas o suplantación de identidad con fines malintencionados.

---

## ✨ Características
- **Identidades Aleatorias:** Generación de nombres, apellidos y datos de perfil realistas.
- **Correos de 10 Minutos:** Integración con APIs de correos desechables para evitar el spam en tu bandeja principal.
- **Seguridad:** Generación de contraseñas robustas para cada identidad creada.
- **Privacidad:** Ideal para registrarse en sitios web de dudosa confianza sin exponer datos reales.

---

## 🛠️ Tecnologías y Conceptos Básicos

Para que este proyecto funcione, utilizamos conceptos clave de programación:

* **APIs (Application Programming Interface):** El script se conecta a servidores externos para obtener correos válidos en tiempo real.
* **Módulo `random`:** Se usa para seleccionar nombres y datos de una base de datos de manera aleatoria.
* **Módulo `string`:** Permite construir contraseñas combinando letras, números y símbolos.

### **¿Dónde descargar las librerías?**
Para este proyecto solemos usar la librería `requests`. Puedes instalarla con:
```bash
pip install requests
