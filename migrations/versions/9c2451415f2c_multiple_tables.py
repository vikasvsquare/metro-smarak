"""Multiple tables

Revision ID: 9c2451415f2c
Revises:
Create Date: 2024-03-20 16:51:29.467181

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9c2451415f2c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "admin_review",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("year_month", sa.Date(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("month", sa.Integer(), nullable=True),
        sa.Column("fiscal_year", sa.String(), nullable=True),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("line_name", sa.String(), nullable=True),
        sa.Column("section_heading", sa.String(), nullable=True),
        sa.Column("comments", sa.String(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "arrest",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("year_month", sa.Date(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("month", sa.Integer(), nullable=True),
        sa.Column("fiscal_year", sa.String(), nullable=True),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("line_name", sa.String(), nullable=True),
        sa.Column("gender", sa.String(), nullable=True),
        sa.Column("ethinicity", sa.String(), nullable=True),
        sa.Column("station_name", sa.String(), nullable=True),
        sa.Column("agency_name", sa.String(), nullable=True),
        sa.Column("arrest_count", sa.Integer(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "arrest_landing",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("current_year_month", sa.Date(), nullable=True),
        sa.Column("current_month_count", sa.Integer(), nullable=True),
        sa.Column("current_year_count", sa.Integer(), nullable=True),
        sa.Column("previous_year_count", sa.Integer(), nullable=True),
        sa.Column("previous_year_count_percent", sa.Integer(), nullable=True),
        sa.Column("previous_month_count", sa.Integer(), nullable=True),
        sa.Column("previous_month_count_percent", sa.Integer(), nullable=True),
        sa.Column("admin_review_id", sa.Integer(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "calls_for_service",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("year_month", sa.Date(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("month", sa.Integer(), nullable=True),
        sa.Column("fiscal_year", sa.String(), nullable=True),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("line_name", sa.String(), nullable=True),
        sa.Column("call_type", sa.String(), nullable=True),
        sa.Column("station_name", sa.String(), nullable=True),
        sa.Column("agency_name", sa.String(), nullable=True),
        sa.Column("calls_count", sa.Integer(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "calls_for_service_landing",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("current_year_month", sa.Date(), nullable=True),
        sa.Column("current_month_count", sa.Integer(), nullable=True),
        sa.Column("current_year_count", sa.Integer(), nullable=True),
        sa.Column("previous_year_month_count", sa.Integer(), nullable=True),
        sa.Column("previous_year_month_count_percent", sa.Integer(), nullable=True),
        sa.Column("previous_month_count", sa.Integer(), nullable=True),
        sa.Column("previous_month_count_percent", sa.Integer(), nullable=True),
        sa.Column("admin_review_id", sa.Integer(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "crime_landing",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("current_year_month", sa.Date(), nullable=True),
        sa.Column("current_month_count", sa.Integer(), nullable=True),
        sa.Column("current_year_count", sa.Integer(), nullable=True),
        sa.Column("total_boardings", sa.Integer(), nullable=True),
        sa.Column("crime_per_100k_boardings", sa.Integer(), nullable=True),
        sa.Column("previous_year_count", sa.Integer(), nullable=True),
        sa.Column("previous_year_count_percent", sa.Integer(), nullable=True),
        sa.Column("previous_month_count", sa.Integer(), nullable=True),
        sa.Column("previous_month_count_percent", sa.Integer(), nullable=True),
        sa.Column("admin_review_id", sa.Integer(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "crime_unvetted",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("year_month", sa.Date(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("month", sa.Integer(), nullable=True),
        sa.Column("fiscal_year", sa.String(), nullable=True),
        sa.Column("week_no", sa.Integer(), nullable=True),
        sa.Column("from_date", sa.Date(), nullable=True),
        sa.Column("to_date", sa.Date(), nullable=True),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("line_name", sa.String(), nullable=True),
        sa.Column("severity", sa.String(), nullable=True),
        sa.Column("ucr", sa.String(), nullable=True),
        sa.Column("crime_name", sa.String(), nullable=True),
        sa.Column("station_name", sa.String(), nullable=True),
        sa.Column("agency_name", sa.String(), nullable=True),
        sa.Column("crime_count", sa.Integer(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "crime_vetted",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("year_month", sa.Date(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("month", sa.Integer(), nullable=True),
        sa.Column("fiscal_year", sa.String(), nullable=True),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("line_name", sa.String(), nullable=True),
        sa.Column("severity", sa.String(), nullable=True),
        sa.Column("ucr", sa.String(), nullable=True),
        sa.Column("crime_name", sa.String(), nullable=True),
        sa.Column("station_name", sa.String(), nullable=True),
        sa.Column("agency_name", sa.String(), nullable=True),
        sa.Column("crime_count", sa.Integer(), nullable=True),
        sa.Column("published", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "location",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("transport_type", sa.String(), nullable=True),
        sa.Column("station_name", sa.String(), nullable=True),
        sa.Column("line_name", sa.String(), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "riders_summary",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("month_number", sa.Integer(), nullable=True),
        sa.Column("day_type", sa.String(), nullable=True),
        sa.Column("line_name", sa.String(), nullable=True),
        sa.Column("provider", sa.String(), nullable=True),
        sa.Column("date_count", sa.Integer(), nullable=True),
        sa.Column("avg_daily_riders", sa.Float(), nullable=True),
        sa.Column("avg_daily_pmiles", sa.Float(), nullable=True),
        sa.Column("riders_total", sa.Integer(), nullable=True),
        sa.Column("pmiles_total", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("riders_summary")
    op.drop_table("location")
    op.drop_table("crime_vetted")
    op.drop_table("crime_unvetted")
    op.drop_table("crime_landing")
    op.drop_table("calls_for_service_landing")
    op.drop_table("calls_for_service")
    op.drop_table("arrest_landing")
    op.drop_table("arrest")
    op.drop_table("admin_review")
    # ### end Alembic commands ###
