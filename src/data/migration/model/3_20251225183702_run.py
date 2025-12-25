from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `run` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `type` VARCHAR(10) NOT NULL COMMENT 'CHAT: chat\nCOMPLETION: completion\nAGENT: agent\nBATCH: batch\nSYSTEM: system\nEVAL: eval' DEFAULT 'chat',
    `status` VARCHAR(7) NOT NULL COMMENT 'PENDING: pending\nRUNNING: running\nSUCCESS: success\nFAILED: failed\nTIMEOUT: timeout' DEFAULT 'pending',
    `owner_type` VARCHAR(6) NOT NULL COMMENT 'USER: user\nAGENT: agent\nSYSTEM: system' DEFAULT 'user',
    `owner_id` CHAR(36),
    `entrypoint` VARCHAR(128) NOT NULL,
    `input_payload` JSON NOT NULL,
    `output_payload` JSON,
    `error` LONGTEXT,
    `meta` JSON,
    KEY `idx_run_created_5a4eb3` (`created_at`),
    KEY `idx_run_updated_c20c42` (`updated_at`),
    KEY `idx_run_deleted_d2ff04` (`deleted_at`)
) CHARACTER SET utf8mb4 COMMENT='Run';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `run`;"""


MODELS_STATE = (
    "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"
)
