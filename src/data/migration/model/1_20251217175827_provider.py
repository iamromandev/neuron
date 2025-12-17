from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `provider` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `name` VARCHAR(64) NOT NULL UNIQUE,
    `slug` VARCHAR(64) NOT NULL UNIQUE,
    `meta` JSON,
    KEY `idx_provider_created_1a0189` (`created_at`),
    KEY `idx_provider_updated_318c28` (`updated_at`),
    KEY `idx_provider_deleted_24350e` (`deleted_at`)
) CHARACTER SET utf8mb4 COMMENT='Provider';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `provider`;"""


MODELS_STATE = (
    "eJztll1v2jAUhv9KlCsmVVwwxMU0TaKUqUwDqha2qVUVmdgEC8dOE3stQvz3+pg4Hw5DGm"
    "s3TeoNxO85ds55Xtnx1o8FJqx9lYqfFJPU/+BtfY5ioh/c0JnnoyQpAjCWaMFMalJNWmQy"
    "RaHU+hKxjGgJkyxMaSKp4JBdXRKLUKdTHukAV4xpSXH6oEggRUTkytR0d69lyjF5IpkdJu"
    "tgSQnDtZIphjWNHshNYrT5fHTx2WTC6xZBKJiKeZmdbORK8CJdKYrbMAdiEeEkRZLgSjNQ"
    "Zd63lfYVa0GmihSl4lLAZIkUAyT+x6XiIZDwzJvgp/vJb0DKWRzAEwoOgCmXwGK723dV9m"
    "xUH141uOxft9733pkuRSaj1AQNEX9nJiKJ9lMN1xJkmBJoO0CyCfRCRySNyWGo9ZkOXJxP"
    "bduHUyBb4QhlS+80pL5uAU852+RLH0E8G42HN7P++AoaibPsgRlC/dkQIh2jbhy1tXdE6E"
    "2y3z3FIt730ezSg6F3O50MXd+KvNmtDzUhJUXAxWOAcIWCVS0pnVn6qhJ8oq/1mW++/ktf"
    "8+JLW/V5TE6ztT7zBWzNq/17rv4nLloOR7en+W84OFih9LB7Nt/xTeN5na/XH+6/GD0FjP"
    "BIrvSw1z3i3Lf+tfl69bqOG5M80jGhXY1exlT0O/Rs/hs9c6sjEjXpfbmZTg7Ts/kOvTnX"
    "fd1hGsozj9FM3r/ImVHeJF/90ICOa+eFhdYa93+4PAdfp+fuQQALnGu4cEtdrivXKxAWKF"
    "w/ohQHjYjoiF/lNkNxJ3YVxFFkWEHHu90zyd7Kyg=="
)
