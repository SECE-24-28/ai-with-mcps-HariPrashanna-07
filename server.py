from mcp.server.fastmcp import FastMCP
from resume_tool import analyze_resume

mcp = FastMCP("Resume Analyzer")

@mcp.tool()
def analyze(text: str):
    """
    Analyze resume text and return ATS score.
    """
    return analyze_resume(text)

if __name__ == "__main__":
    mcp.run()
