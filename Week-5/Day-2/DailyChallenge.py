# Instructions :
# 1 - Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# 2 - The Pagination class will accept 2 parameters:
#       - items (default: []): A list of contents to paginate.
#       - pageSize (default: 10): The amount of items to show in each page.

# 3 - The Pagination class will have a few methods:
#       - getVisibleItems() : returns a list of items visible depending on the pageSize
#       - You will have to implement various methods to go through the pages such as:
#           - prevPage()
#           - nextPage()
#           - firstPage()
#           - lastPage()
#           - goToPage(pageNum)

# Notes:

# - The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# - The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# - Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# - If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).



class Pagination():
    """
    this method is used to divide long lists of content in a series of pages.
    """
    
    def __init__(self:object, items = [], pageSize = 10, top_of_page = 0, current_page = 1  ) -> object:
        self.items = items
        self.pageSize = int(pageSize)
        self.end_of_page = int(pageSize)
        self.top_of_page = int(top_of_page)
        self.current_page = int(current_page)
        self.total_pages = len(items)

    
    def getVisibleItems(self:object) -> None:
        """
        display the items according to the pageSize
        """
        if self.end_of_page > self.total_pages:
            self.top_of_page = self.end_of_page - self.pageSize
            self.end_of_page = self.total_pages
            print("You are on the last page ...")

        if self.top_of_page < 0:
            self.top_of_page = 0
            self.end_of_page = self.pageSize
            print("You are on the first page ...")

        print(f"PAGE {self.current_page}")
        for item in range(self.top_of_page, self.end_of_page):
            print(self.items[item])

        print("-----------")
    
    def nextPage(self:object):
        """
        go to the next page by jumping the amount of pageSize on the list and iniate the curentepage var 
        """

        self.top_of_page += self.pageSize
        self.end_of_page += self.pageSize

        if not self.end_of_page > self.total_pages:
            self.current_page += 1

        return self

    def prevPage(self:object):
        """
        go to the previous page by jumping the amount of pageSize on the list and iniate the curentepage var 
        """

        self.top_of_page -= self.pageSize
        self.end_of_page -= self.pageSize

        if not self.top_of_page < 0:
            self.current_page -= 1

        return self
    
    def firstPage(self:object) -> None:
        """
        go to the first page
        """

        self.end_of_page = self.pageSize
        self.top_of_page = 0
        self.current_page = 1
        self.total_pages = len(self.items)

    
    def lastPage(self:object) -> None:
        """
        go to the last page
        """

        self.top_of_page = self.end_of_page - self.pageSize
        self.end_of_page = self.total_page
        self.current_page = 1
        self.total_pages = len(self.items)


alphabetStr = "abcdefghijklmnopqrstuvwxyz"
alphabetList = list(alphabetStr)

p = Pagination(alphabetList, 4)
p.getVisibleItems()
p.prevPage()
p.getVisibleItems()
p.nextPage
p.getVisibleItems()
p.nextPage().nextPage()
p.getVisibleItems()