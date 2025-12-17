from memory.embeddings import Embedder
import logging

logger = logging.getLogger("MemoryUtils")

def store_failure(memory_db, step_data: dict, reason: str):
    """
    Standardized utility to record a failure.
    Combines the intent, files, and the reason for failure into a single context string.
    """
    embedder = Embedder()
    
    # Create a rich text representation for the vector DB
    context_string = (
        f"Intent: {step_data.get('intent')} | "
        f"Files: {','.join(step_data.get('files', []))} | "
        f"Failure Reason: {reason}"
    )
    
    vector = embedder.embed_text(context_string)
    
    metadata = {
        "step": step_data,
        "reason": reason,
        "timestamp": "2025-12-17" # Dynamic date would go here
    }
    
    memory_db.add(vector, metadata)
    logger.info(f"Memory updated with failure in: {step_data.get('intent')}")

def query_similar_lessons(memory_db, pr_diff: str, top_k: int = 3):
    """
    Given a new PR diff, find the top K most relevant past failures 
    to help the Planner avoid them.
    """
    embedder = Embedder()
    query_vector = embedder.embed_text(pr_diff)
    
    results = memory_db.query(query_vector, k=top_k)
    
    # Format for the LLM prompt
    lessons = []
    for match in results:
        lessons.append({
            "previous_mistake": match['step']['intent'],
            "what_went_wrong": match['reason']
        })
    
    return lessons
