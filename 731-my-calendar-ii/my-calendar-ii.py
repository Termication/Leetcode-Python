class MyCalendarTwo:

    def __init__(self):
                # Stores all bookings
        self.bookings = []
        # Stores all double bookings (overlaps)
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check if this booking would cause a triple booking
        for s, e in self.overlaps:
            if start < e and end > s:  # There is an overlap with a double booking
                return False
        
        # Check for new double bookings with existing single bookings
        for s, e in self.bookings:
            if start < e and end > s:  # There is an overlap
                # Add the overlapping part to the overlaps list
                self.overlaps.append((max(start, s), min(end, e)))
        
        # No triple booking, so add the new booking to the bookings list
        self.bookings.append((start, end))
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)