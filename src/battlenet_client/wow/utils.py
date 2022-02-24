def namespace(api_type, release, region):

    if release.lower() != "retail":
        return f"{api_type}-{release.lower()}-{region.lower()}"

    return f"{api_type}-{region.lower()}"
