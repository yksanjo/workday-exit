"""CLI for WorkdayExit."""

import click
from .assessor import MigrationAssessor


@click.group()
def cli():
    """WorkdayExit - Workday Migration Platform."""
    pass


@cli.command()
@click.option("--employees", required=True, type=int, help="Current number of employees")
@click.option("--current-cost", required=True, type=float, help="Current Workday annual cost")
@click.option("--seat-reduction", default=0.3, type=float, help="Expected headcount reduction (0.0-1.0)")
def assess(employees: int, current_cost: float, seat_reduction: float):
    """Assess Workday usage and calculate migration savings."""
    click.echo(f"📊 Assessing Workday migration for {employees} employees...")
    
    assessor = MigrationAssessor()
    result = assessor.assess(employees, current_cost, seat_reduction)
    
    click.echo(f"\n✅ Assessment Results:")
    click.echo(f"Current Employees: {result['current_employees']}")
    click.echo(f"Reduced Employees: {result['reduced_employees']}")
    click.echo(f"Current Workday Cost: ${result['current_workday_cost']:,.2f}")
    click.echo(f"Alternative Cost: ${result['alternative_cost']:,.2f}")
    click.echo(f"Total Savings: ${result['total_savings']:,.2f} ({result['savings_percentage']:.1f}%)")


@cli.command()
def alternatives():
    """List Workday alternatives."""
    click.echo("🔄 Workday Alternatives:\n")
    click.echo("1. AgentHR - AI-Native HCM Platform")
    click.echo("   - Transaction-based pricing")
    click.echo("   - 60-80% cost savings\n")
    click.echo("2. AgentFinance - AI-Native Finance Platform")
    click.echo("   - Better AI agents than Workday")
    click.echo("   - Multi-platform integration\n")
    click.echo("3. OpenHR - Open-Source HR Platform")
    click.echo("   - Community-driven")
    click.echo("   - No vendor lock-in")


if __name__ == "__main__":
    cli()

