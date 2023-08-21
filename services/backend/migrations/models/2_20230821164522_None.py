from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL,
    "last_login" TIMESTAMPTZ NOT NULL,
    "email" VARCHAR(200) NOT NULL  DEFAULT '',
    "avatar" VARCHAR(200) NOT NULL  DEFAULT '',
    "intro" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "admin"."last_login" IS 'Last Login';
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "full_name" VARCHAR(50),
    "password" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "tasks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(256) NOT NULL,
    "description" TEXT NOT NULL,
    "due_date" TIMESTAMPTZ NOT NULL,
    "completed" BOOL NOT NULL  DEFAULT False,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
