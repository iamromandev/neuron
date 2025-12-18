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
    CONSTRAINT `fk_model_provider_630ed586` FOREIGN KEY (`provider_id`) REFERENCES `provider` (`id`) ON DELETE CASCADE,
    KEY `idx_model_created_a13d08` (`created_at`),
    KEY `idx_model_updated_abb4b5` (`updated_at`),
    KEY `idx_model_deleted_a6da78` (`deleted_at`)
) CHARACTER SET utf8mb4 COMMENT='Model';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `model`;"""


MODELS_STATE = (
    "eJztmltP4zgUgP9KlCdWYhEpFSA0Wiltw04X2qJSZldzUeQmbrDqOJnEgakQ/31t5+6khX"
    "ZaKFJeSnMujs934h7nmCfV9WyIjwb8U71QnlQCXMi+lOSHigp8P5PyawqmGJYkYBrSAFiU"
    "CWcAh5CJbBhaAfIp8gg3zQazPYvZIuIwKYkwZqKIoJ8RNKnnQHoPA6b49oOJEbHhLximl/"
    "7cnCGI7dJMkc3HFHKTLnwhu7vr9y6FJb/d1LQ8HLkkt/YX9N4jmXkUIfuI+3CdAwkMAIV2"
    "IRI+yyTiVBTPmAloEMFsqnYusOEMRJjzUD/NImJxDIq4E/9o/6VWCCUsavBYHuF0EaGcxd"
    "NzHFUes5Cq/Fbdz/r44OT0DxGlF1InEEpBRH0WjoCC2FVwzUFaAeRhm4BWgfaYhiIX1kMt"
    "e0pw7cT1KP2yCeRUsIJySm8zpCoLwR4RvEiGXoF40h8YtxN9cMMDccPwJxaE9InBNS0hXU"
    "jSgzgjHlsh8brJBlH+7U8+K/xS+ToaGnLeMrvJV5XPCUTUM4n3aAK7QCGVpqSYZZ7XyLc3"
    "zGvZs8nre+Y1mXyeVvZjCjdLa9lzC2lNZvt2Wf0gWUw5rFyeIQU0Ctl4lSz+czsa1mew6C"
    "Pl744wlt9sZNFDBaOQ/tjOssxrek1Vm0YIU0TCI37DHRU2DqOU0uEXfSyq3UD/T0rfsHs9"
    "6si54gN0RAkslDzggynCiKL1+Mt+TQ5+IwdMb7Koa37GuvcgMEjkiiT02SwBsWA1GcUBpE"
    "ywwHbG3oeBqc2rpNUbY2xqVxdKbPCdiOvjVHA8X7IHliuXC36ZGBKH3rPLsxVpSZNwJqcg"
    "UbS4pgxd/K3lXf/Ap/Zvh/c3y34J3mn7FfRO20vxcVWZ3wMMQj6lNRAWXDai+HKR3S3Ek9"
    "YrIJ60lkLkqjJE6lGA2TvfHBITI7fuF6BPaD3NWl+JK4tjT59Oh9/nz5bWPmufn5y2z5mJ"
    "mEsmWbXc+8OJBNKLqB/RDUnWO2+E8h0e0S2TRISz4BWlZlMNLeQCvKSvUHKU99Sx51Eywl"
    "6SXIGpZ3T7A/36QDs+jDfKrPojCovrvn0sL+7ksdoApeTZsFRRaKZTq6DseB6GgCx5KkuO"
    "Eskp89zV72N9C3AbADuj0XVpD9rpT6SSczfoGOMDTcJbXewupGCdXX9qv4Xd/l49kzvZ1v"
    "uB94BstuFdrz8ruW2zUfuujF/oy/Lu9mxe25ZNiVQpXnoBRA65govKC5LELe7m3xRG2lt4"
    "uTRfJgF4zBr/8hPCooz7WYKyftvVe4YqeE6BNX8EgW2WwHKN1/IkSWZbVbktV5YAAhzBgE"
    "fC5y3xrR6kFNEvPUspZvrl45TikM2JSnOi0nTemxOVJq/NiUpzohKfjmzaTs6937CXzCo9"
    "eoA1vWS9O+l/MS6U2OA76Rl/j9kOp3eh2NAJgA1tJuvf6p1rIUMhnwaTDXT2vmMM9WGXOb"
    "s8zZBk4a7Z+dO0V3T+NG1p54+r9qn9/PL+Yr+bzyGOnHXopfYNPa6bghCaUYDXIVj0+ZDN"
    "e611/po13Dpfvoi5rumf7LR/UukCLH+NlV4wa6pdJ/G7vBpDDGj90ZP0b34fpyvwvP33+O"
    "f/AZDgMEw="
)
