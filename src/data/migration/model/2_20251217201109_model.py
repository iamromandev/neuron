from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `model` (
    `id` CHAR(36) NOT NULL PRIMARY KEY,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `status` VARCHAR(10) NOT NULL COMMENT 'ACTIVE: active\nINACTIVE: inactive\nDEPRECATED: deprecated\nERROR: error' DEFAULT 'active',
    `name` VARCHAR(64) NOT NULL,
    `total_token_limit` INT NOT NULL,
    `output_token_limit` INT,
    `cost_unit` INT NOT NULL DEFAULT 1000,
    `input_cost` DECIMAL(10,6),
    `output_cost` DECIMAL(10,6),
    `capabilities` JSON NOT NULL,
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
    "eJztmm1v4jgQgP9KlE89qYcoi7qranVSCqk2twtUlO6d9kWRiU1q1bGzidMuqvjvaztvxA"
    "n0ytGWlfIFyHjG8Tzjl/GIBzNgEJHOSH6aZ8aDSUGAxI+K/NgwQRgWUvnMwZygigTMYx4B"
    "jwvhApAYCRFEsRfhkGNGpWrRGWSe0MXUF1KaECJECcU/EuRy5iN+gyLR8PW7EGMK0U8U54"
    "/hrbvAiMDKSDGUfSq5y5ehkl1fO8MLpSlfN3c9RpKAltrhkt8wWqgnCYYdaSPbfERRBDiC"
    "a57IUWYe56J0xELAowQVQ4WlAKIFSIjkYb5fJNSTGAz1JvnR/8usEcpYNODxGJV0MeWSxc"
    "Mq9ar0WUlN+arBB2t69Ob0D+Uli7kfqUZFxFwpQ8BBaqq4liC9CEm3XcDrQIeiheMANUOt"
    "WmpwYWbayX/sAjkXbKGc09sNqSlcgBNKllnXWxDPnJF9NbNGl9KRII5/EEXImtmypaekS0"
    "16lEaEiRWSrpuiE+MfZ/bBkI/Gl8nY1uNW6M2+mHJMIOHMpezeBXCNQi7NSQnNMq5JCHeM"
    "a9WyjetrxjUbfBlWsZmi3cJatdxDWLPRvlxUf5Mo5hy2Ls+YA57E9RgObkBk0yRQMXSE+4"
    "B6qBbL0lqLo8C1nwVZnubFeSaOeXyH6geYaQ1mzmf7zEgVvlFnnEswzWVD+3JqDwT54ZkB"
    "URghTw7vG7Wn08n0zEBRxKINWYK+tgPw0yWI+vxGPJ50t8yKz9ZUnYwnXS3S46ylp5pWlc"
    "io78a4NK+rXP/lIvE/98YKv9P+f+B32t/ITzZV+XHGARE53S2iLsEBbtioHMqbWTbaamCF"
    "HwcK1pfv+bN30n/bf/fmtP9OqKixFJK3W1g745kGkiU8TPiOJJuNd0L5+D5/6CQ9sXm7Yv"
    "xPAVixebkpeNLtdg8HHKZyEkkUDdkG8nAAyIYLV8VQTzZSy07Ww0FOwS2YhvbAGVmfxNFx"
    "nGYQIq/AHK1vmP3aqZKtxx1QapYtS9MDIZhjoYdRQwb199VkvGFJa3Yaymsq/PoKscePDY"
    "Jj/v3ZMqmyMjBPMOGYxh35wmcqDkgglbQ4P72PRta/+sE++DQ51/Nd2cG5FoMAcfAU9rn+"
    "Hpgf1AR+FrhhxO4wRJH7tCqXZrbPcterMn6kuiVrhIvbxuJWTqRO8YJFCPv0I1rWbloat7"
    "QmernW08HCK6XlMonAfVE+1WeI8DKtCijK1tXAGtqm4jkH3u09iKBbAStbWI9pkkK33hT0"
    "Al0CKPAVA+mJHLfGt16OXke/sSK9HunHi9LrXbZ16bYu3dYv27p0G9e2Lt3WpV+3+vn46X"
    "XYtc+YJP5T6OX6LT2zvVOae79T1m5Gm1N7LeluqKucZ3YXH6eIAOVunb32B5Lf56a02v/d"
    "ZvUL8udgBA=="
)
