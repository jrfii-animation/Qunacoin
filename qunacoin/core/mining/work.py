WORKLOADS = {
    "qml": qml_workloads,
    "optimization": optimization_workloads,
    "physics": physics_workloads, 
    "math": math_workloads,
}

def execute_job(job_data):
    """Execute a proof-of-computation workload job"""
    job_type = job_data["type"]
    
    if job_type not in WORKLOADS:
        return None
        
    module = WORKLOADS[job_type]
    result = module.execute(job_data)
    
    # Validate result
    is_valid = module.validate(job_data, result)
    
    if not is_valid:
        return None
        
    return result