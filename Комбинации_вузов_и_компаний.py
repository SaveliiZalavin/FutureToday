{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMCUDPFy1WgnwzEYMPDF88Y",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SaveliiZalavin/FutureToday/blob/main/%D0%9A%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8_%D0%B2%D1%83%D0%B7%D0%BE%D0%B2_%D0%B8_%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B9.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "26wlhEZ56M9L"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "import itertools\n",
        "\n",
        "def load_table(path):\n",
        "    if path.endswith(\".csv\"):\n",
        "        return pd.read_csv(path)\n",
        "    elif path.endswith(\".xlsx\") or path.endswith(\".xls\"):\n",
        "        return pd.read_excel(path)\n",
        "    else:\n",
        "        raise ValueError(\"Формат файла должен быть CSV или Excel (.xlsx)\")\n",
        "\n",
        "def make_pairs(unis_file, comps_file):\n",
        "    # ---- загрузка ----\n",
        "    df_unis = load_table(unis_file)\n",
        "    df_comps = load_table(comps_file)\n",
        "\n",
        "    # ---- поиск колонок ----\n",
        "    # ищем колонку uni (без учёта регистра)\n",
        "    uni_col = [c for c in df_unis.columns if c.lower() == \"uni\"]\n",
        "    if not uni_col:\n",
        "        raise ValueError(\"В таблице с университетами нет колонки 'uni'\")\n",
        "    uni_col = uni_col[0]\n",
        "\n",
        "    # ищем колонку Comp (без учёта регистра)\n",
        "    comp_col = [c for c in df_comps.columns if c.lower() == \"comp\"]\n",
        "    if not comp_col:\n",
        "        raise ValueError(\"В таблице с компаниями нет колонки 'Comp'\")\n",
        "    comp_col = comp_col[0]\n",
        "\n",
        "    unis = df_unis[uni_col].dropna().unique().tolist()\n",
        "    comps = df_comps[comp_col].dropna().unique().tolist()\n",
        "\n",
        "    # ---- все комбинации ----\n",
        "    pairs = list(itertools.product(unis, comps))\n",
        "    df_out = pd.DataFrame(pairs, columns=[\"uni\", \"comp\"])\n",
        "\n",
        "    return df_out\n",
        "\n",
        "\n",
        "# -------------------------\n",
        "# Пример использования\n",
        "# -------------------------\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    df_result = make_pairs(\"unis.csv\", \"companies.csv\") # Изменено расширение файлов на .csv\n",
        "\n",
        "    print(df_result)\n",
        "    df_result.to_csv(\"uni_comp_pairs.csv\", index=False)\n",
        "    df_result.to_excel(\"uni_comp_pairs.xlsx\", index=False)"
      ]
    }
  ]
}