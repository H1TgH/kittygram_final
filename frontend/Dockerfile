FROM node:18 AS builder
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM alpine:latest

COPY --from=builder /app/build /usr/share/nginx/html

CMD ["cp", "-r", "/usr/share/nginx/html/.", "/frontend_static/"]