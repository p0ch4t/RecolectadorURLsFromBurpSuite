# RecolectadorURLsFromBurpSuite

Python script que permite a partir de un file XML exportado desde el Proxy History de Burp Suite, parsear las URLs e imprimirlas por pantalla.

Pasos para su ejecución:
1. Vaya a Burp Suite, en la pestaña HTTP History, seleccione las URLs que quiere exportar y haga click derecho "Save Items"
2. Luego de haber guardado el archivo XML, ejecute: python3 RecolectadorURLsFromBurpSuite.py archivo.xml
3. Verá que se le imprime las URLs por pantalla.

Versionado de [https://github.com/mrts/burp-suite-http-proxy-history-converter](https://github.com/mrts/burp-suite-http-proxy-history-converter)