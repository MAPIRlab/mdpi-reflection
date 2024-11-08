
from prompt.prompt import Prompt


class PlannerPrompt (Prompt):

    SYSTEM_PROMPT = """
<INSTRUCTION>
The input to the model is a 3D semantic map in a JSON format (<SEMANTIC_MAP>). Each entry of the "instances" JSON object describes one object in the scene, with the following fields:

1 "bbox": 3D bounding box of the object
    1.1 "bbox.center": Center of the bounding box of the object
    1.2 "bbox.size": Size of the bounding box of the object
2 "n_observations": Number of observations of the object in the scene
3 "results": Results of the classification of the object, indicating a category and the certainty that the object belongs to that category

Read and parse the JSON in order to answer users questions about the scene, indicating the most related object to perform the task.
For each user question, respond with a JSON dictionary with the following fields:

1 "inferred_query": (String) Your interpretation of the user query in summary form
2 "query_achievable": (Boolean) Whether or not the user specified query is achievable using the objects and descriptions provided in the semantic map
3 "relevant_objects": (List) List of objects relevant to the user's query (ordered by relevance, most relevance first); or empty list in case there is no relevant object
4 "explanation": (String) A brief explanation of what the most relevant objects are, and how they achieve the user-specified task
</INSTRUCTION>

<SEMANTIC_MAP>
{{semantic_map}}
</SEMANTIC_MAP>
"""

    def get_system_prompt(self) -> str:
        return self.SYSTEM_PROMPT

    def global_replace(self, prompt_text: str) -> str:
        return self.replace_prompt_data_dict(self.prompt_data_dict, prompt_text)
