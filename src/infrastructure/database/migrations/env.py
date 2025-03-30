from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from src.config.config import config
from src.infrastructure.database.config import Base

from src.infrastructure.database.models import UserModel, PostModel, CommentModel


config_alembic = context.config


if config_alembic.config_file_name is not None:
    fileConfig(config_alembic.config_file_name)


target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=config.DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(config.DATABASE_URL, poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()



if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()