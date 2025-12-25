from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `model` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `statuses` JSON NOT NULL,
    `capabilities` JSON NOT NULL,
    `cost_unit` VARCHAR(7) NOT NULL COMMENT 'PER_1K: per_1k\nPER_10K: per_10k' DEFAULT 'per_1k',
    `name` VARCHAR(64) NOT NULL,
    `version` VARCHAR(32),
    `total_token_limit` INT NOT NULL,
    `output_token_limit` INT,
    `input_cost` DECIMAL(10,6),
    `output_cost` DECIMAL(10,6),
    `is_default` BOOL NOT NULL DEFAULT 0,
    `meta` JSON,
    `provider_id` CHAR(36) NOT NULL,
    UNIQUE KEY `uid_model_provide_28c4f4` (`provider_id`, `name`, `version`),
    CONSTRAINT `fk_model_provider_630ed586` FOREIGN KEY (`provider_id`) REFERENCES `provider` (`id`) ON DELETE CASCADE,
    KEY `idx_model_created_a13d08` (`created_at`),
    KEY `idx_model_updated_abb4b5` (`updated_at`),
    KEY `idx_model_deleted_a6da78` (`deleted_at`)
) CHARACTER SET utf8mb4 COMMENT='Model';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `model`;"""


MODELS_STATE = (
    "eJztmu1P6joYwP8Vsk/exEscEjXm5CYD5j1cBQziuTfHY5ayldnQdTtbp4cY//fbdu/dQO"
    "CAouEL0uel9Pk969o+9VlxXAvieo9/Kue1Z4UAB7IvBflhTQGel0p5m4IxhgUJGAfUByZl"
    "wgnAAWQiCwamjzyKXMJN084s12S2iNhMSkKMmSgk6GcIDerakD5Anynu7hTPdx+RxVrMQI"
    "yL/X2EfsD7u79nDUQs+AsG3Jo3vakxQRBbhUCQxd2E3KAzT8hub7udC2HJRzM2TBeHDsms"
    "vRl9cElqHobIqnMfrrMhgT6g0MoFyoOIgSSiKCAmoH4I06FamcCCExBijkv5MgmJySnVxC"
    "/xj+ZfSglgjKqCnukSDh8Rylk8v0RRZTELqcJ/qv1VGx4cn/whonQDavtCKYgoL8IRUBC5"
    "Cq4ZSNOHPGwD0DLQDtNQ5MBqqEVPCa4Vu9aTL+tATgQLKCf01kOqsBCsAcGzuOsFiEfdnn"
    "4z0nrXPBAnCH5iQUgb6VzTENKZJD2IMuKyCRRNq7ST2r/d0dcab9a+D/q6nLfUbvRd4WMC"
    "IXUN4j4ZwMpRSKQJKWaZ5TX0rDXzWvTc5/U98xoPPksre9fC9dJa9NxAWuPRvl1WP0gWEw"
    "4Lp2dAAQ0D1l8pi//cDPrVGcz7SPm7JYzlnYVMeljDKKD3m5mW2ZJfsaqNQ4QpIkGd/+CW"
    "FjYOo5DS/jdtKFa7nvaflL5++2rQknPFO2iJJTC35AEPjBFGFK3GX/bb5+A3csD0Bou64j"
    "XWfgC+TkJHJKHLRgmICcvJyHcgZYIFtjX2HvQNdVomrVzrQ0O9PK9FBj+IaB8lgqPpnC2y"
    "vHI54JeBIbHpA2ueLkhLkoRTOQWxosE1RejJbrvMu/qBT+zfDu9vLvsFeCfNJeidNOfi46"
    "oiv+SUsgLCnMtaFF9fZLcL8bixBMTjxlyIXFWESF0KMDsSTiExMHKq3gBdQqtpVvpKXFkc"
    "O/p02vx3/myozdPm2fFJ84yZiLGkkkXTvdsfSSDdkHohXZNktfNaKN/hEd0wSUQ4C76iVG"
    "yqoYkcgOfUFQqO8p468qzHPewkyQWYOnq729OuDtSjw2ijzFZ/RGF+3jeP5MkdP1ZroJQ8"
    "9ywVFBjJ0EooW66LISBznsqCo0RyzDy39X6srhBuAmBrMLgq7EFb3ZG05Nz2WvrwQJXwli"
    "e7AylYZdef2G9gt79Tz+RWtvVJbddYrT4ruW2yUPuujF+py/Lq9mRaWZbNF8mLFC9cHyKb"
    "XMJZ6YAkcYuK/de5nnYWXibNpokPntLCv/yEsCijepagrN20tY6uCJ5jYE6fgG8ZBbBc4z"
    "ZcSZLallVOw5ElgABbMOCR8HFLfMv3LHn0c69a8pl+/bYl3+VyFy77G5UtzNzD/Y3KJ6+8"
    "729UPmde9zcqn/pGZd1ycub9hrVkttKjR1hRS9bao+43/bwWGfwgHf3vIdvhdM5rFrR9YE"
    "GLybo3WutKyFDAh8FkPY2dd/S+1m8zZ4enGZI03BUrf6q6ROVPVedW/rhql8rPr+8vdrv4"
    "HODQXoVeYr+nx3VjEEAj9PEqBPM+H7J4rzbOlpnDjbP5k5jr9vWTrdZPSlWA+cdY6YBZsd"
    "q1Yr+LyyHEgFZfPUn/BfhxqgIvmz/Hv/wPHr46eg=="
)
