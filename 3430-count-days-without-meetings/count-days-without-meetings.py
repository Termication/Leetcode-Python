class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        Counts the number of days without meetings.

        Args:
            days: The total number of working days.
            meetings: A list of meetings, where meetings[i] = [start_i, end_i].

        Returns:
            The number of days without meetings.
        """
        meetings.sort()
        
        merged_meetings = []
        for meeting in meetings:
            if not merged_meetings or meeting[0] > merged_meetings[-1][1]:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])
        
        meeting_days_count = 0
        for start, end in merged_meetings:
            meeting_days_count += end - start + 1
        
        return days - meeting_days_count
        