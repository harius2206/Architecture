class EnumerableMethods:
    @staticmethod
    def to_line_list(collection, prompt: str) -> str:
        result = f"{prompt}:\n"
        lines = "\n".join([str(item) for item in collection])
        return result + lines + "\n"