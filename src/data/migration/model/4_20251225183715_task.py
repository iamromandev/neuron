from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `task` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `name` VARCHAR(128) NOT NULL,
    `status` VARCHAR(9) NOT NULL COMMENT 'PENDING: pending\nRUNNING: running\nCOMPLETED: completed\nFAILED: failed' DEFAULT 'pending',
    `input_payload` JSON NOT NULL,
    `output_payload` JSON,
    `error` LONGTEXT,
    `meta` JSON,
    `run_id` CHAR(36) NOT NULL,
    CONSTRAINT `fk_task_run_c9b4fa90` FOREIGN KEY (`run_id`) REFERENCES `run` (`id`) ON DELETE CASCADE,
    KEY `idx_task_created_afb134` (`created_at`),
    KEY `idx_task_updated_57b925` (`updated_at`),
    KEY `idx_task_deleted_938c7f` (`deleted_at`)
) CHARACTER SET utf8mb4 COMMENT='Task';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `task`;"""


MODELS_STATE = (
    "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"
    "PC5/8BufU8fg=="
)
