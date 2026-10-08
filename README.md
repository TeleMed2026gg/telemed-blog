# Blog Telemed: telemed.com.co/blog

Blog estático (HTML puro) generado con `build.py`, con el mismo diseño de telemed.com.co/us.

## Cómo funciona

```
drafts/          ← borradores semanales (NO se suben a GitHub)
content/         ← artículos aprobados (se suben y se publican)
_internal/       ← guía de marca y plan de palabras clave (NO se sube)
build.py         ← genera el sitio
.github/workflows/deploy.yml ← GitHub construye y publica en la rama "deploy"
```

Flujo semanal:

1. **Lunes:** la tarea programada de Claude deja 3 borradores en inglés y 1 en español en `drafts/`.
2. **Revisión:** abres cada borrador y le agregas un dato o una anécdota real. Revisas que no haya afirmaciones prohibidas (ver `_internal/brand-guide.md`).
3. **Aprobar:** mueves el archivo de `drafts/en/` a `content/en/` (o de `drafts/es/` a `content/es/`) y cambias `status: draft` por `status: published`. También le puedes pedir a Claude: "publica los borradores de esta semana".
4. **Publicar:** en github.com/TeleMed2026gg/telemed-blog → *Add file → Create new file*, nombre `content/en/<slug>.md`, pegar el contenido y *Commit changes*. GitHub genera el sitio y lo sube por FTP a telemed.com.co/blog/ en 1 a 2 minutos.

## Vista previa local
`python build.py --preview` genera `preview/`, que incluye también los borradores.

## Reglas de calidad (resumen)
- Máximo 3 artículos en inglés y 1 en español por semana. Más volumen genérico es riesgo de penalización de Google.
- Cada cifra externa debe llevar su fuente enlazada.
- Seguir la guía editorial interna (no publicar precios, no inventar testimonios).
