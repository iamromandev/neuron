from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `call` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `status` VARCHAR(7) NOT NULL COMMENT 'PENDING: pending\nRUNNING: running\nSUCCESS: success\nFAILED: failed\nTIMEOUT: timeout' DEFAULT 'pending',
    `prompt_tokens` INT,
    `output_tokens` INT,
    `total_tokens` INT,
    `cost` DECIMAL(12,6),
    `input_payload` JSON NOT NULL,
    `output_payload` JSON,
    `latency_ms` INT,
    `error` LONGTEXT,
    `meta` JSON,
    `model_id` CHAR(36) NOT NULL,
    `provider_id` CHAR(36) NOT NULL,
    `task_id` CHAR(36) NOT NULL,
    CONSTRAINT `fk_call_model_b54ba699` FOREIGN KEY (`model_id`) REFERENCES `model` (`id`) ON DELETE RESTRICT,
    CONSTRAINT `fk_call_provider_55ed20d2` FOREIGN KEY (`provider_id`) REFERENCES `provider` (`id`) ON DELETE RESTRICT,
    CONSTRAINT `fk_call_task_d9103aad` FOREIGN KEY (`task_id`) REFERENCES `task` (`id`) ON DELETE CASCADE,
    KEY `idx_call_created_5dffa5` (`created_at`),
    KEY `idx_call_updated_9f3709` (`updated_at`),
    KEY `idx_call_deleted_7dadee` (`deleted_at`)
) CHARACTER SET utf8mb4 COMMENT='Call';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `call`;"""


MODELS_STATE = (
    "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"
    "+z7SxkL94nXbkEu0r6ztTd8///tne8"
)
