# -*- coding: utf-8 -*-
"""
TURKPATENT MCP Server

MCP server for searching Turkish trademarks, patents, and designs
on turkpatent.gov.tr using FastMCP.

Usage:
    python mcp_server.py          # Direct run (stdio)
    fastmcp dev mcp_server.py     # Development mode
    fastmcp run mcp_server.py     # Production mode
"""

from typing import Optional, Literal, Annotated
from fastmcp import FastMCP, Context
from pydantic import Field

from core import (
    search_trademarks_core,
    get_trademark_detail_core,
    search_patents_core,
    get_patent_detail_core,
    search_designs_core,
    get_design_detail_core,
)


# --- FastMCP Server ---

mcp = FastMCP(
    name="TURKPATENT MCP",
    instructions="""
    TURKPATENT Trademark, Patent and Design Search MCP Server.

    This server provides access to the Turkish Patent and Trademark Office
    (turkpatent.gov.tr) research database.

    Features:
    - Trademark search and detail retrieval
    - Patent search and detail retrieval
    - Industrial design search and detail retrieval

    All searches support pagination. Detail queries return full application information.
    Note: Automatically handles reCAPTCHA protection via capsolver.
    """,
)


# --- Trademark Tools ---

@mcp.tool
async def search_trademarks(
    trademark_name: Annotated[str, Field(description="Trademark name to search for")] = "",
    name_operator: Annotated[
        Literal["contains", "startsWith", "equals"],
        Field(description="Search operator for trademark name"),
    ] = "contains",
    holder_name: Annotated[
        Optional[str],
        Field(description="Trademark holder/applicant name"),
    ] = None,
    holder_name_operator: Annotated[
        Literal["startsWith", "equals"],
        Field(description="Search operator for holder name"),
    ] = "startsWith",
    nice_classes: Annotated[
        Optional[str],
        Field(description="Nice classification codes, comma-separated (e.g. '9,35,42')"),
    ] = None,
    limit: Annotated[int, Field(ge=1, le=100, description="Results per page")] = 20,
    offset: Annotated[int, Field(ge=0, description="Pagination offset")] = 0,
    ctx: Context = None,
) -> dict:
    """
    Search trademarks registered in Turkey on TURKPATENT.

    Returns a list of matching trademarks with application number, name, holder,
    status, Nice classes, and application date.

    Examples:
    - search_trademarks(trademark_name="Apple")
    - search_trademarks(trademark_name="Samsung", nice_classes="9,35")
    - search_trademarks(holder_name="VESTEL")
    """
    if ctx:
        await ctx.info(f"Searching trademarks: '{trademark_name or '*'}' (offset={offset})")

    try:
        result = await search_trademarks_core(
            trademark_name=trademark_name,
            name_operator=name_operator,
            holder_name=holder_name,
            holder_name_operator=holder_name_operator,
            nice_classes=nice_classes,
            limit=limit,
            offset=offset,
        )
        if ctx:
            await ctx.info(f"Found {len(result.get('items', []))} trademarks (total: {result.get('total', 0)})")
        return result

    except Exception as e:
        error_msg = f"Trademark search error: {e}"
        if ctx:
            await ctx.error(error_msg)
        return {"error": error_msg, "total": 0, "items": []}


@mcp.tool
async def get_trademark_details(
    application_number: Annotated[str, Field(description="Trademark application number (e.g. 'T/01853', '2020/12345')")],
    ctx: Context = None,
) -> dict:
    """
    Get detailed information about a specific trademark application.

    Returns mark information including name, holder, Nice classes, application date,
    registration status, bulletin numbers, and protection dates.
    """
    if ctx:
        await ctx.info(f"Fetching trademark details: {application_number}")

    try:
        result = await get_trademark_detail_core(application_number)
        if ctx:
            await ctx.info("Trademark details retrieved")
        return result

    except Exception as e:
        error_msg = f"Trademark detail error: {e}"
        if ctx:
            await ctx.error(error_msg)
        return {"error": error_msg}


# --- Patent Tools ---

@mcp.tool
async def search_patents(
    title: Annotated[str, Field(description="Invention title to search for")] = "",
    abstract: Annotated[Optional[str], Field(description="Invention abstract keywords")] = None,
    owner: Annotated[Optional[str], Field(description="Inventor name")] = None,
    applicant: Annotated[Optional[str], Field(description="Patent applicant name")] = None,
    application_number: Annotated[Optional[str], Field(description="Patent application number")] = None,
    ipc_class: Annotated[Optional[str], Field(description="IPC classification code")] = None,
    cpc_class: Annotated[Optional[str], Field(description="CPC classification code")] = None,
    attorney: Annotated[Optional[str], Field(description="Patent attorney name")] = None,
    limit: Annotated[int, Field(ge=1, le=100, description="Results per page")] = 20,
    offset: Annotated[int, Field(ge=0, description="Pagination offset")] = 0,
    ctx: Context = None,
) -> dict:
    """
    Search patents registered in Turkey on TURKPATENT.

    Returns matching patents with application number, title, applicant,
    IPC class, and publication date.

    Examples:
    - search_patents(title="yapay zeka")
    - search_patents(applicant="ASELSAN")
    - search_patents(ipc_class="G06F")
    """
    if ctx:
        await ctx.info(f"Searching patents: '{title or '*'}' (offset={offset})")

    try:
        result = await search_patents_core(
            title=title,
            abstract=abstract,
            owner=owner,
            applicant=applicant,
            application_number=application_number,
            ipc_class=ipc_class,
            cpc_class=cpc_class,
            attorney=attorney,
            limit=limit,
            offset=offset,
        )
        if ctx:
            await ctx.info(f"Found {len(result.get('items', []))} patents (total: {result.get('total', 0)})")
        return result

    except Exception as e:
        error_msg = f"Patent search error: {e}"
        if ctx:
            await ctx.error(error_msg)
        return {"error": error_msg, "total": 0, "items": []}


@mcp.tool
async def get_patent_details(
    application_number: Annotated[str, Field(description="Patent application number")],
    ctx: Context = None,
) -> dict:
    """
    Get detailed information about a specific patent application.

    Returns full patent information including title, abstract, inventors,
    applicant, IPC/CPC classes, priority claims, and publication dates.
    """
    if ctx:
        await ctx.info(f"Fetching patent details: {application_number}")

    try:
        result = await get_patent_detail_core(application_number)
        if ctx:
            await ctx.info("Patent details retrieved")
        return result

    except Exception as e:
        error_msg = f"Patent detail error: {e}"
        if ctx:
            await ctx.error(error_msg)
        return {"error": error_msg}


# --- Design Tools ---

@mcp.tool
async def search_designs(
    design_name: Annotated[str, Field(description="Design name to search for")] = "",
    designer: Annotated[Optional[str], Field(description="Designer name")] = None,
    applicant: Annotated[Optional[str], Field(description="Design applicant name")] = None,
    registration_no: Annotated[Optional[str], Field(description="Design registration number")] = None,
    locarno_class: Annotated[Optional[str], Field(description="Locarno classification code")] = None,
    attorney: Annotated[Optional[str], Field(description="Design attorney name")] = None,
    limit: Annotated[int, Field(ge=1, le=100, description="Results per page")] = 20,
    offset: Annotated[int, Field(ge=0, description="Pagination offset")] = 0,
    ctx: Context = None,
) -> dict:
    """
    Search industrial designs registered in Turkey on TURKPATENT.

    Returns matching designs with registration number, design name,
    applicant, Locarno class, and bulletin information.

    Examples:
    - search_designs(design_name="masa")
    - search_designs(applicant="IKEA")
    - search_designs(locarno_class="06-01")
    """
    if ctx:
        await ctx.info(f"Searching designs: '{design_name or '*'}' (offset={offset})")

    try:
        result = await search_designs_core(
            design_name=design_name,
            designer=designer,
            applicant=applicant,
            registration_no=registration_no,
            locarno_class=locarno_class,
            attorney=attorney,
            limit=limit,
            offset=offset,
        )
        if ctx:
            await ctx.info(f"Found {len(result.get('items', []))} designs (total: {result.get('total', 0)})")
        return result

    except Exception as e:
        error_msg = f"Design search error: {e}"
        if ctx:
            await ctx.error(error_msg)
        return {"error": error_msg, "total": 0, "items": []}


@mcp.tool
async def get_design_details(
    file_id: Annotated[str, Field(description="Design file ID from search results (e.g. '106417')")],
    ctx: Context = None,
) -> dict:
    """
    Get detailed information about a specific design application.

    Use the fileId value from search_designs results to retrieve full details.
    Returns design information including design name, designer,
    applicant, Locarno class, registration details, and bulletin dates.
    """
    if ctx:
        await ctx.info(f"Fetching design details: {file_id}")

    try:
        result = await get_design_detail_core(file_id)
        if ctx:
            await ctx.info("Design details retrieved")
        return result

    except Exception as e:
        error_msg = f"Design detail error: {e}"
        if ctx:
            await ctx.error(error_msg)
        return {"error": error_msg}


# --- Entry Point ---

def main():
    """Entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
