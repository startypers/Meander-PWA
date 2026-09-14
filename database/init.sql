-- Создание таблицы для интересных мест (POI - Points of Interest)
CREATE TABLE IF NOT EXISTS pois (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    description TEXT,
    geom GEOMETRY(Point, 4326) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Индекс для быстрого поиска точек в радиусе
CREATE INDEX idx_pois_geom ON pois USING GIST (geom);

-- Примеры категорий: park, street_art, viewpoint, historic_building, cafe
