class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # Process the ppid to make a map in between parent and children to avoid multiple N look ups
        parent_children_process_map = {}
        for i, parent in enumerate(ppid):
            parent_children_process_map[parent] = parent_children_process_map.get(parent, [])
            parent_children_process_map[parent].append(pid[i])
        # Use a queue to process the elements that need to be eliminated
        # The process consist in look in to their children and add them to the target list and queue
        queue = [kill]
        process_to_kill = []
        while queue:
            process = queue.pop()
            process_to_kill.append(process)
            children = parent_children_process_map.get(process)
            if children:
                queue.extend(children)
        
        return process_to_kill