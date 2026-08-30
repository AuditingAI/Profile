# Application runner — containerised.
#
# The container holds the CODE. It never holds credentials.
#
# Sessions live in a Docker volume mounted at /sessions, which maps to a
# directory on your own machine. You log in once, in a real browser window,
# and the cookie lands there. Nothing under /sessions is ever copied into
# this image, committed to git, or transmitted anywhere.
#
# Build:  docker compose build
# Login:  docker compose run --rm login      (one time per employer portal)
# Apply:  docker compose run --rm apply

FROM mcr.microsoft.com/playwright:v1.49.0-noble

WORKDIR /app

# Dependencies first so a code change doesn't reinstall Chromium.
COPY package.json ./
RUN npm install --omit=dev

# Application code only. The .dockerignore keeps sessions/ and any stray
# credential file out of the build context entirely — belt and braces, so
# even a mistake in this COPY cannot bake a secret into a layer.
COPY apply_runner.mjs ./

# Where the persistent browser profile is mounted. Declared as a VOLUME so
# Docker refuses to persist it into a committed image layer.
VOLUME ["/sessions"]
ENV RUNNER_PROFILE_DIR=/sessions/browser-profile

# Run as the image's non-root user so files written to the mounted volume
# are not owned by root on your host.
USER pwuser

ENTRYPOINT ["node", "apply_runner.mjs"]
