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
    "Inf/ecyX/wFrN9pp"
)
