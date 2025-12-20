"""Migration assessment tool."""

from typing import Dict, Any
from datetime import datetime


class MigrationAssessor:
    """Assess Workday usage and calculate migration savings."""
    
    def assess(self, employees: int, current_cost: float, seat_reduction: float = 0.3) -> Dict[str, Any]:
        """
        Assess Workday usage and calculate migration savings.
        
        Args:
            employees: Current number of employees
            current_cost: Current Workday annual cost
            seat_reduction: Expected headcount reduction (default 30%)
            
        Returns:
            Assessment results
        """
        reduced_employees = int(employees * (1 - seat_reduction))
        workday_savings = current_cost * seat_reduction
        alternative_cost = current_cost * 0.2  # 80% savings with transaction-based
        
        return {
            "current_employees": employees,
            "reduced_employees": reduced_employees,
            "current_workday_cost": current_cost,
            "workday_savings": workday_savings,
            "alternative_cost": alternative_cost,
            "total_savings": current_cost - alternative_cost,
            "savings_percentage": ((current_cost - alternative_cost) / current_cost) * 100,
            "assessment_date": datetime.utcnow().isoformat()
        }

