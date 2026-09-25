{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOJZPWUgVeqWaEQoo1H74Rp",
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
        "<a href=\"https://colab.research.google.com/github/NareshSahu7/Libron/blob/main/WORLD_CUP_ANALYSIS.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ma6DqvesWwdv",
        "outputId": "34c3ae98-5501-4252-946c-192310cffaae"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "ICC Men's Cricket World Cup Data Analysis\n"
          ]
        }
      ],
      "source": [
        "print(\"ICC Men's Cricket World Cup Data Analysis\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "print(\"All libraries imported successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rSqtCbyHXfQi",
        "outputId": "be321f5b-019a-41c9-c949-ea4c42b5cb44"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "All libraries imported successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = {\n",
        "    \"Year\": [1975, 1979, 1983, 1987, 1992, 1996, 1999, 2003, 2007, 2011, 2015, 2019, 2023],\n",
        "\n",
        "    \"Winner\": [\n",
        "        \"West Indies\",\n",
        "        \"West Indies\",\n",
        "        \"India\",\n",
        "        \"Australia\",\n",
        "        \"Pakistan\",\n",
        "        \"Sri Lanka\",\n",
        "        \"Australia\",\n",
        "        \"Australia\",\n",
        "        \"Australia\",\n",
        "        \"India\",\n",
        "        \"Australia\",\n",
        "        \"England\",\n",
        "        \"Australia\"\n",
        "    ]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "b2HFtKCuYKSs",
        "outputId": "4f66369a-464a-46e9-d4eb-e23d8d0f18cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    Year       Winner\n",
            "0   1975  West Indies\n",
            "1   1979  West Indies\n",
            "2   1983        India\n",
            "3   1987    Australia\n",
            "4   1992     Pakistan\n",
            "5   1996    Sri Lanka\n",
            "6   1999    Australia\n",
            "7   2003    Australia\n",
            "8   2007    Australia\n",
            "9   2011        India\n",
            "10  2015    Australia\n",
            "11  2019      England\n",
            "12  2023    Australia\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.DataFrame(data)"
      ],
      "metadata": {
        "id": "Yghp0m1XYfR3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'cricket_data'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "eaNiqZaAYutl",
        "outputId": "12c27b92-d14c-4e27-da40-fd9a41acb4aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'cricket_data'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 457
        },
        "id": "pI1VFjC-Y0O3",
        "outputId": "f2e10194-a077-459b-a498-3226493fdead"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Year       Winner\n",
              "0   1975  West Indies\n",
              "1   1979  West Indies\n",
              "2   1983        India\n",
              "3   1987    Australia\n",
              "4   1992     Pakistan\n",
              "5   1996    Sri Lanka\n",
              "6   1999    Australia\n",
              "7   2003    Australia\n",
              "8   2007    Australia\n",
              "9   2011        India\n",
              "10  2015    Australia\n",
              "11  2019      England\n",
              "12  2023    Australia"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-7e1a1129-53b8-443e-91db-a764e0bf27d8\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Year</th>\n",
              "      <th>Winner</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1975</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1979</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1983</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1987</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1992</td>\n",
              "      <td>Pakistan</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>1996</td>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>1999</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2003</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>2007</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>2011</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>2015</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>2019</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>2023</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7e1a1129-53b8-443e-91db-a764e0bf27d8')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-7e1a1129-53b8-443e-91db-a764e0bf27d8 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-7e1a1129-53b8-443e-91db-a764e0bf27d8');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_6a33bbb6-0f2e-40a6-afce-dd1938ac4992\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_6a33bbb6-0f2e-40a6-afce-dd1938ac4992 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 13,\n  \"fields\": [\n    {\n      \"column\": \"Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15,\n        \"min\": 1975,\n        \"max\": 2023,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          2019,\n          2011,\n          1975\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Winner\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"West Indies\",\n          \"India\",\n          \"England\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "Ov7UZtmdY_gY",
        "outputId": "79c16779-6d93-4b99-efd0-f572c3ca67ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Year       Winner\n",
              "0  1975  West Indies\n",
              "1  1979  West Indies\n",
              "2  1983        India\n",
              "3  1987    Australia\n",
              "4  1992     Pakistan"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-83f7f040-f1ba-4de8-9196-fe47e236ef14\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Year</th>\n",
              "      <th>Winner</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1975</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1979</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1983</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1987</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1992</td>\n",
              "      <td>Pakistan</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-83f7f040-f1ba-4de8-9196-fe47e236ef14')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-83f7f040-f1ba-4de8-9196-fe47e236ef14 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-83f7f040-f1ba-4de8-9196-fe47e236ef14');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 13,\n  \"fields\": [\n    {\n      \"column\": \"Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15,\n        \"min\": 1975,\n        \"max\": 2023,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          2019,\n          2011,\n          1975\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Winner\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"West Indies\",\n          \"India\",\n          \"England\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GL5T1s1LZOwf",
        "outputId": "611aa885-0e96-4def-b043-d432c6d9ad30"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 13 entries, 0 to 12\n",
            "Data columns (total 2 columns):\n",
            " #   Column  Non-Null Count  Dtype \n",
            "---  ------  --------------  ----- \n",
            " 0   Year    13 non-null     int64 \n",
            " 1   Winner  13 non-null     object\n",
            "dtypes: int64(1), object(1)\n",
            "memory usage: 340.0+ bytes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "winner_count = df[\"Winner\"].value_counts()\n",
        "\n",
        "print(winner_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Kk_WMmooZVDU",
        "outputId": "b793472e-0e80-4c58-aca4-06a7a8ae0fd3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Winner\n",
            "Australia      6\n",
            "West Indies    2\n",
            "India          2\n",
            "Pakistan       1\n",
            "Sri Lanka      1\n",
            "England        1\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "winner_count.plot(kind=\"bar\")\n",
        "\n",
        "plt.title(\"ICC Men's Cricket World Cup Winners\")\n",
        "plt.xlabel(\"Team\")\n",
        "plt.ylabel(\"Number of Titles\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 537
        },
        "id": "pA507B0lZnK0",
        "outputId": "8f1ea8b7-8fed-4dc1-c5b9-7910e0b6101b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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r6+v6tevr2PHjj1SEdu3b9fEiRNVsmTJR3o8AAB4MjkdVPLmzastW7YoJiZGq1at0gsvvCBJunTpktKmTet0AVevXlWrVq00efJkZcqU6YFt4+LiFB0d7XADAABPLqeDSs+ePdWqVSvlyZNHOXPmVI0aNSTdOSVUokQJpwvo1q2b6tevrzp16jy07YgRIxQQEGC/5c2b1+nXAwAA7sPL2Qd07dpV5cuXV1RUlJ5//nl5eNzJOvnz53d6jMqcOXO0a9cubd++PVntBw4cqN69e9vvR0dHE1YAAHiCOR1UJKlcuXIqWbKkIiMjFRoaKi8vL9WvX9+p54iKilKPHj30888/J/uUkY+Pj3x8fB6lZAAA4IacPvUTGxur9u3by9fXV8WKFdOZM2ckSe+8845GjhyZ7OfZuXOnzp07pzJlysjLy0teXl7asGGDxowZIy8vL92+fdvZ0gAAwBPG6aAycOBA7d27V+vXr3foCalTp47mzp2b7OepXbu29u/frz179thv5cqVU6tWrbRnzx55eno6WxoAAHjCOH3qZ8mSJZo7d64qVqwom81m316sWDGdOHEi2c/j5+en4sWLO2xLnz69smTJkmg7AAB4Ojndo3L+/HkFBgYm2h4TE+MQXAAAAB6X0z0q5cqV048//qh33nlHkuzhZMqUKapUqdJjFbN+/frHejwAAHiyOB1Uhg8frrp16+rQoUO6deuWvvrqKx06dEgRERHasGFDStQIAACeUk6f+gkLC9OePXt069YtlShRQj/99JMCAwO1ZcsWlS1bNiVqBAAAT6lHWkclNDRUkydPdnUtAAAADpIVVJy5po6/v/8jFwMAAHC3ZAWVjBkzPnRGj2EYstlsLNQGAABcJllBZd26dSldBwAAQCLJCirVq1e3//vMmTPKmzdvoh4WwzAUFRXl2uoAAMBTzelZPyEhITp//nyi7RcvXlRISIhLigIAAJAeIagkjEW519WrV5N9FWQAAIDkSPb05N69e0u6sxLtoEGD5Ovra993+/Zt/fbbbypdurTLCwQAAE+vZAeV3bt3S7rTo7J//355e3vb93l7e6tUqVLq27ev6ysEAABPrWQHlYSZP23bttVXX33FeikAACDFOb0y7fTp01OiDgAAgESSFVSaNm2qGTNmyN/fX02bNn1g20WLFrmkMAAAgGQFlYCAAPtMn4CAgBQtCAAAIEGygsr06dM1dOhQ9e3bl1M/AAAg1SR7HZXw8HBdvXo1JWsBAABwkOygYhhGStYBAACQiFMr0z7sCsoAAACu5NT05EKFCj00rFy8ePGxCgIAAEjgVFAJDw9n1g8AAEg1TgWVFi1aKDAwMKVqAQAAcJDsMSqMTwEAAKmNWT8AAMCykn3qJz4+PiXrAAAASMSp6ckAAACpiaACAAAsi6ACAAAsK1lBpUyZMrp06ZIkaejQoYqNjU3RogAAAKRkBpXDhw8rJiZGEhcnBAAAqSdZs35Kly6ttm3bKiwsTIZh6LPPPlOGDBmSbPvhhx+6tEAAAPD0SlZQmTFjhgYPHqzly5fLZrNp5cqV8vJK/FCbzUZQAQAALpOsoFK4cGHNmTNHkuTh4aE1a9awlD4AAEhxTl3rR2LhNwAAkHqcDiqSdOLECY0ePVqHDx+WJBUtWlQ9evRQaGioS4sDAABPN6fXUVm9erWKFi2qbdu2qWTJkipZsqR+++03FStWTD///HNK1AgAAJ5STveoDBgwQL169dLIkSMTbX/33Xf1/PPPu6w4AADwdHO6R+Xw4cNq3759ou3t2rXToUOHXFIUAACA9AhBJVu2bNqzZ0+i7Xv27GEmEAAAcCmnT/107NhRnTp10smTJ1W5cmVJ0ubNmzVq1Cj17t3b5QUCAICnl9NBZdCgQfLz89Pnn3+ugQMHSpJy5cqlIUOGqHv37i4vEAAAPL2cDio2m029evVSr169dOXKFUmSn5+fywsDAAB4pHVUEhBQAABASnJ6MC0AAEBqIagAAADLIqgAAADLciqo3Lx5U7Vr19axY8dSqh4AAAA7p4JKmjRptG/fPpe9+IQJE1SyZEn5+/vL399flSpV0sqVK132/AAAwL05fern9ddf19SpU13y4nny5NHIkSO1c+dO7dixQ7Vq1VLjxo118OBBlzw/AABwb05PT75165amTZumX375RWXLllX69Okd9n/xxRfJfq6GDRs63P/44481YcIEbd26VcWKFXO2NAAA8IRxOqgcOHBAZcqUkSQdPXrUYZ/NZnvkQm7fvq358+crJiZGlSpVSrJNXFyc4uLi7Pejo6Mf+fUAAID1OR1U1q1b59IC9u/fr0qVKun69evKkCGDFi9erKJFiybZdsSIEQoPD3fp6wMAAOt65OnJx48f1+rVq3Xt2jVJkmEYj/Q8hQsX1p49e/Tbb7+pS5cuat26tQ4dOpRk24EDB+ry5cv2W1RU1KOWDwAA3IDTPSoXLlxQ8+bNtW7dOtlsNh07dkz58+dX+/btlSlTJn3++edOPZ+3t7cKFCggSSpbtqy2b9+ur776ShMnTkzU1sfHRz4+Ps6WDAAA3JTTPSq9evVSmjRpdObMGfn6+tq3v/rqq1q1atVjFxQfH+8wDgUAADy9nO5R+emnn7R69WrlyZPHYXvBggV1+vRpp55r4MCBqlu3roKCgnTlyhXNnj1b69ev1+rVq50tCwAAPIGcDioxMTEOPSkJLl686PRpmXPnzunNN9/UX3/9pYCAAJUsWVKrV6/W888/72xZAADgCeR0UKlatapmzZqlYcOGSbozJTk+Pl6ffPKJatas6dRzuWrhOAAA8GRyOqh88sknql27tnbs2KEbN26of//+OnjwoC5evKjNmzenRI0AAOAp5fRg2uLFi+vo0aMKCwtT48aNFRMTo6ZNm2r37t0KDQ1NiRoBAMBTyukeFUkKCAjQ+++/7+paAAAAHDxSULl06ZKmTp2qw4cPS5KKFi2qtm3bKnPmzC4tDgAAPN2cPvWzceNG5cuXT2PGjNGlS5d06dIljRkzRiEhIdq4cWNK1AgAAJ5STveodOvWTa+++qomTJggT09PSXcuKNi1a1d169ZN+/fvd3mRAADg6eR0j8rx48fVp08fe0iRJE9PT/Xu3VvHjx93aXEAAODp5nRQKVOmjH1syt0OHz6sUqVKuaQoAAAAKZmnfvbt22f/d/fu3dWjRw8dP35cFStWlCRt3bpV48aN08iRI1OmSgAA8FSyGYZhPKyRh4eHbDabHtbUZrPp9u3bLivuYaKjoxUQEKDLly/L39/fZc+bb8CPLnuulHJqZH2zSwAA4JE48/mdrB6VyMhIlxQGAADgjGQFleDg4JSuAwAAIJFHWvDtzz//1KZNm3Tu3DnFx8c77OvevbtLCgMAAHA6qMyYMUOdO3eWt7e3smTJIpvNZt9ns9kIKgAAwGWcDiqDBg3Shx9+qIEDB8rDw+nZzQAAAMnmdNKIjY1VixYtCCkAACDFOZ022rdvr/nz56dELQAAAA6cPvUzYsQINWjQQKtWrVKJEiWUJk0ah/1ffPGFy4oDAABPt0cKKqtXr1bhwoUlKdFgWgAAAFdxOqh8/vnnmjZtmtq0aZMC5QAAAPwfp8eo+Pj4qEqVKilRCwAAgAOng0qPHj309ddfp0QtAAAADpw+9bNt2zatXbtWy5cvV7FixRINpl20aJHLigMAAE83p4NKxowZ1bRp05SoBQAAwIHTQWX69OkpUQcAAEAiLC8LAAAsy+kelZCQkAeul3Ly5MnHKggAACCB00GlZ8+eDvdv3ryp3bt3a9WqVerXr5+r6gIAAHA+qPTo0SPJ7ePGjdOOHTseuyAAAIAELhujUrduXS1cuNBVTwcAAOC6oLJgwQJlzpzZVU8HAADg/KmfZ5991mEwrWEYOnv2rM6fP6/x48e7tDgAAPB0czqoNGnSxOG+h4eHsmXLpho1aqhIkSKuqgsAAMD5oDJ48OCUqAMAACARFnwDAACWleweFQ8Pjwcu9CZJNptNt27deuyiAAAAJCeCyuLFi++7b8uWLRozZozi4+NdUhQAAIDkRFBp3Lhxom1HjhzRgAEDtGzZMrVq1UpDhw51aXEAAODp9khjVP7880917NhRJUqU0K1bt7Rnzx7NnDlTwcHBrq4PAAA8xZwKKpcvX9a7776rAgUK6ODBg1qzZo2WLVum4sWLp1R9AADgKZbsUz+ffPKJRo0apRw5cuiHH35I8lQQAACAK9kMwzCS09DDw0Pp0qVTnTp15Onped92ixYtcllxDxMdHa2AgABdvnxZ/v7+LnvefAN+dNlzpZRTI+ubXQIAAI/Emc/vZPeovPnmmw+dngwAAOBKyQ4qM2bMSMEyAAAAEmNlWgAAYFkEFQAAYFkEFQAAYFkEFQAAYFmmBpURI0boueeek5+fnwIDA9WkSRMdOXLEzJIAAICFmBpUNmzYoG7dumnr1q36+eefdfPmTb3wwguKiYkxsywAAGARyZ6enBJWrVrlcH/GjBkKDAzUzp07Va1aNZOqAgAAVmFqULnX5cuXJUmZM2dOcn9cXJzi4uLs96Ojo1OlLgAAYA7LBJX4+Hj17NlTVapUue9FDkeMGKHw8PBUrgyPyh0uRSC5x+UI3OFYusNxBOB+LDPrp1u3bjpw4IDmzJlz3zYDBw7U5cuX7beoqKhUrBAAAKQ2S/SovP3221q+fLk2btyoPHny3Ledj4+PfHx8UrEyAABgJlODimEYeuedd7R48WKtX79eISEhZpYDAAAsxtSg0q1bN82ePVv//e9/5efnp7Nnz0qSAgIClC5dOjNLAwAAFmDqGJUJEybo8uXLqlGjhnLmzGm/zZ0718yyAACARZh+6gcAAOB+LDPrBwAA4F4EFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFmmBpWNGzeqYcOGypUrl2w2m5YsWWJmOQAAwGJMDSoxMTEqVaqUxo0bZ2YZAADAorzMfPG6deuqbt26yW4fFxenuLg4+/3o6OiUKAsAAFiEqUHFWSNGjFB4eLjZZQBwY/kG/Gh2CQ91amR9s0t4KHc4jhLH0lXMPI5uNZh24MCBunz5sv0WFRVldkkAACAFuVWPio+Pj3x8fMwuAwAApBK36lEBAABPF4IKAACwLFNP/Vy9elXHjx+334+MjNSePXuUOXNmBQUFmVgZAACwAlODyo4dO1SzZk37/d69e0uSWrdurRkzZphUFQAAsApTg0qNGjVkGIaZJQAAAAtjjAoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsggoAALAsSwSVcePGKV++fEqbNq0qVKigbdu2mV0SAACwANOD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3Dqo0KOSiq5fvy5PT0+WhgYAuFShQoVUr149DR8+PNF15twdQQUAHsP169d148YNh21c3gGpLX369Nq/f7/y589vdiku514L/rsJDw8PeXp63veG5KlVq5b+/fffRNujo6NVq1at1C8I+P9iYmL09ttvKzAwUOnTp1emTJkcbkBqe/HFF7Vjxw6zy0gRjFFJAYsXL3a4f/PmTe3evVszZ85UeHi4SVW5n/Xr1yf6pird+Qb766+/mlARcEf//v21bt06TZgwQW+88YbGjRunP/74QxMnTky04Bb+D1egTjn169dXv379dOjQoSQv4tqoUSOTKnt8nPpJRbNnz9bcuXP13//+1+xSLC1hZdrSpUtr7dq1Dlecvn37tlatWqWJEycyewqmCQoK0qxZs1SjRg35+/tr165dKlCggL799lv98MMPWrFihdklWpKnp6f9CtQeHh5cgdqFHnRFZHc/nvSopKKKFSuqU6dOZpdheQkr09pstiRP8aRLl05ff/21CZUBd1y8eNE+FsDf398+HTksLExdunQxszRLu/uLx7p160yu5sly73TkJwlBJZVcu3ZNY8aMUe7cuc0uxfIiIyNlGIby58+vbdu2KVu2bPZ93t7eCgwMZKwPTJU/f35FRkYqKChIRYoU0bx581S+fHktW7ZMGTNmNLs8y0q44vmtW7e0YcMGtWvXTnny5DG5KvdWr149/fDDDwoICJAkjRw5Um+99Zb99/DChQuqWrWqDh06ZGKVj4dTPyng3oWhDMPQlStXlC5dOn3//fdufa4QgPTll1/K09NT3bt31y+//KKGDRvKMAzdvHlTX3zxhXr06GF2iZbn5+en/fv3u/3y7ma7+3SadKeHb8+ePfYev7///lu5cuXi1A8c3bswlIeHh7Jly6YKFSpwwS0nzJw5U1mzZlX9+vUl3RnAOGnSJBUtWlQ//PAD1/pBqouPj9enn36qpUuX6saNG/rzzz81ePBg/f7779q5c6cKFCjAVb2TqVatWtqwYQNB5THd29fwJPY90KOSCq5cuaIffvhBU6dO1Y4dO9w62aamwoULa8KECapVq5a2bNmi2rVra/To0Vq+fLm8vLy0aNEis0vEU2bYsGEaMmSI6tSpo3Tp0mn16tVq2bKlpk2bZnZpbuebb75ReHi4WrVqpbJlyyp9+vQO++l5Th4PDw+dPXvW3qPi5+envXv3PlE9KgSVFLRx40ZNnTpVCxcuVK5cudS0aVM1a9bMfgluPJivr69+//13BQUF6d1339Vff/2lWbNm6eDBg6pRo4bOnz9vdol4yhQsWFB9+/ZV586dJUm//PKL6tevr2vXrj1w1gUSe5JnqaQmT09PnT171j6Wz8/PT/v27bNfpfpJCCqc+nGxs2fPasaMGZo6daqio6PVvHlzxcXFacmSJSpatKjZ5bmVDBky6MKFCwoKCtJPP/2k3r17S5LSpk3LFahhijNnzqhevXr2+3Xq1JHNZtOff/7JoFAnPcmzVFKTYRhq06aNfHx8JN1ZZ+qtt96y91DFxcWZWZ5LEFRcqGHDhtq4caPq16+v0aNH66WXXpKnp6e++eYbs0tzS88//7w6dOigZ599VkePHrV/QBw8eJDz2jDFrVu3lDZtWodtadKk0c2bN02qCE+71q1bO9x//fXXE7Vx5wsSSgQVl1q5cqW6d++uLl26qGDBgmaX4/bGjRunDz74QFFRUVq4cKGyZMkiSdq5c6datmxpcnV4Gt377VVK/A1WEuOnHmDLli26cOGCGjRoYN82a9YsDR48WDExMWrSpIm+/vprh2OM+5s+fbrZJaQ4xqi40NatWzV16lTNnTtXzzzzjN544w21aNFCOXPm1N69ezn1A7i5tm3bJqvd0/Dh8ajq1q2rGjVq6N1335Uk7d+/X2XKlFGbNm30zDPP6NNPP1Xnzp01ZMgQcwuFZRBUUkBMTIzmzp2radOmadu2bbp9+7a++OILtWvXTn5+fmaX51Z+/fVXTZw4USdPntT8+fOVO3duffvttwoJCVFYWJjZ5QFwUs6cObVs2TKVK1dOkvT+++9rw4YN2rRpkyRp/vz5Gjx4sFsvUAbXYph6CkifPr3atWunTZs2af/+/erTp49GjhypwMBAptw5YeHChXrxxReVLl067dq1yz4o7PLlyxo+fLjJ1QF4FJcuXVL27Nnt9zds2KC6deva7z/33HOKiooyozRYFEElhRUuXFiffPKJ/ve//+mHH34wuxy38tFHH+mbb77R5MmTHa4EWqVKFe3atcvEygA8quzZsysyMlKSdOPGDe3atUsVK1a0779y5UqiK//i6UZQSSWenp5q0qSJli5danYpbuPIkSOqVq1aou0BAQH6999/U78gAI+tXr16GjBggH799VcNHDhQvr6+qlq1qn3/vn37FBoaamKFsBqCCiwrR44cOn78eKLtmzZtsq+6CMC9DBs2TF5eXqpevbomT56syZMny9vb275/2rRpeuGFF0ysEFbD9GRYVseOHdWjRw9NmzbNvqjWli1b1LdvXw0aNMjs8gA8gqxZs2rjxo26fPmyMmTIkOhK6PPnz1eGDBlMqg5WxKwfWJZhGBo+fLhGjBih2NhYSZKPj4/69u2rYcOGmVwdACA1EFRgOZGRkfbrVEh3BtwdP35cV69eVdGiRfm2BQBPEYIKLMfDw0PBwcGqWbOmatWqpZo1ayp37txmlwUAMAFBBZazfv16++23337TjRs3lD9/fntoqVmzpsM6DACAJxdBBZZ2/fp1RURE2IPLtm3bdPPmTRUpUkQHDx40uzwAQAojqMAt3LhxQ5s3b9bKlSs1ceJEXb16Vbdv3za7LABACiOowJJu3LihrVu3at26dfZTQHnz5lW1atVUrVo1Va9eXUFBQWaXCQBIYQQVWE6tWrX022+/KSQkRNWrV1fVqlVVvXp15cyZ0+zSAACpjKACy0mTJo1y5sypJk2aqEaNGqpevbqyZMlidlkAABMQVGA5MTEx+vXXX7V+/XqtW7dOe/bsUaFChVS9enV7cMmWLZvZZQIAUgFBBZZ35coVbdq0yT5eZe/evSpYsKAOHDhgdmkAgBTGRQlheenTp1fmzJmVOXNmZcqUSV5eXjp8+LDZZQEAUgE9KrCc+Ph47dixw37qZ/PmzYqJiVHu3LntC77VrFlTwcHBZpcKAEhhBBVYjr+/v2JiYpQjRw57KKlRo4ZCQ0PNLg0AkMoIKrCciRMnqmbNmipUqJDZpQAATEZQAQAAlsVgWgAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAAYFkEFQAuZ7PZHngbMmSI2SUCcBNeZhcA4Mnz119/2f89d+5cffjhhzpy5Ih9W4YMGcwoC4AbokcFgMvlyJHDfgsICJDNZnPYNmfOHD3zzDNKmzatihQpovHjxzs8/t1331WhQoXk6+ur/Pnza9CgQbp586Z9/5AhQ1S6dGlNmzZNQUFBypAhg7p27arbt2/rk08+UY4cORQYGKiPP/44td86ABejRwVAqvr+++/14YcfauzYsXr22We1e/dudezYUenTp1fr1q0lSX5+fpoxY4Zy5cql/fv3q2PHjvLz81P//v3tz3PixAmtXLlSq1at0okTJ/Sf//xHJ0+eVKFChbRhwwZFRESoXbt2qlOnjipUqGDW2wXwmFiZFkCKmjFjhnr27Kl///1XklSgQAENGzZMLVu2tLf56KOPtGLFCkVERCT5HJ999pnmzJmjHTt2SLrTo/Lpp5/q7Nmz8vPzkyS99NJLOnLkiE6cOCEPjzudxUWKFFGbNm00YMCAFHyHAFISPSoAUk1MTIxOnDih9u3bq2PHjvbtt27dUkBAgP3+3LlzNWbMGJ04cUJXr17VrVu35O/v7/Bc+fLls4cUScqePbs8PT3tISVh27lz51LwHQFIaQQVAKnm6tWrkqTJkycnOh3j6ekpSdqyZYtatWql8PBwvfjiiwoICNCcOXP0+eefO7RPkyaNw32bzZbktvj4eFe/DQCpiKACINVkz55duXLl0smTJ9WqVask20RERCg4OFjvv/++fdvp06dTq0QAFkNQAZCqwsPD1b17dwUEBOill15SXFycduzYoUuXLql3794qWLCgzpw5ozlz5ui5557Tjz/+qMWLF5tdNgCTMD0ZQKrq0KGDpkyZounTp6tEiRKqXr26ZsyYoZCQEElSo0aN1KtXL7399tsqXbq0IiIiNGjQIJOrBmAWZv0AAADLokcFAABYFkEFAABYFkEFAABYFkEFAABYFkEFAABYFkEFAABYFkEFAABYFkEFAABYFkEFAABYFkEFAABYFkEFAABY1v8D7NUt/rP3ZtsAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# ICC Men's Cricket World Cup data\n",
        "\n",
        "world_cup_data = {\n",
        "    \"Year\": [1975, 1979, 1983, 1987, 1992, 1996, 1999,\n",
        "             2003, 2007, 2011, 2015, 2019, 2023],\n",
        "\n",
        "    \"Host\": [\n",
        "        \"England\",\n",
        "        \"England\",\n",
        "        \"England\",\n",
        "        \"India & Pakistan\",\n",
        "        \"Australia & New Zealand\",\n",
        "        \"India, Pakistan & Sri Lanka\",\n",
        "        \"England\",\n",
        "        \"South Africa\",\n",
        "        \"West Indies\",\n",
        "        \"India, Sri Lanka & Bangladesh\",\n",
        "        \"Australia & New Zealand\",\n",
        "        \"England & Wales\",\n",
        "        \"India\"\n",
        "    ],\n",
        "\n",
        "    \"Winner\": [\n",
        "        \"West Indies\",\n",
        "        \"West Indies\",\n",
        "        \"India\",\n",
        "        \"Australia\",\n",
        "        \"Pakistan\",\n",
        "        \"Sri Lanka\",\n",
        "        \"Australia\",\n",
        "        \"Australia\",\n",
        "        \"Australia\",\n",
        "        \"India\",\n",
        "        \"Australia\",\n",
        "        \"England\",\n",
        "        \"Australia\"\n",
        "    ],\n",
        "\n",
        "    \"Runner_Up\": [\n",
        "        \"Australia\",\n",
        "        \"England\",\n",
        "        \"West Indies\",\n",
        "        \"England\",\n",
        "        \"England\",\n",
        "        \"Australia\",\n",
        "        \"Pakistan\",\n",
        "        \"India\",\n",
        "        \"Sri Lanka\",\n",
        "        \"Sri Lanka\",\n",
        "        \"New Zealand\",\n",
        "        \"New Zealand\",\n",
        "        \"India\"\n",
        "    ]\n",
        "}\n",
        "\n",
        "world_cup_df = pd.DataFrame(world_cup_data)\n",
        "\n",
        "world_cup_df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 457
        },
        "id": "yJudBiikZwMD",
        "outputId": "b61c577b-9df7-4714-9c1f-bbee44d11191"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Year                           Host       Winner    Runner_Up\n",
              "0   1975                        England  West Indies    Australia\n",
              "1   1979                        England  West Indies      England\n",
              "2   1983                        England        India  West Indies\n",
              "3   1987               India & Pakistan    Australia      England\n",
              "4   1992        Australia & New Zealand     Pakistan      England\n",
              "5   1996    India, Pakistan & Sri Lanka    Sri Lanka    Australia\n",
              "6   1999                        England    Australia     Pakistan\n",
              "7   2003                   South Africa    Australia        India\n",
              "8   2007                    West Indies    Australia    Sri Lanka\n",
              "9   2011  India, Sri Lanka & Bangladesh        India    Sri Lanka\n",
              "10  2015        Australia & New Zealand    Australia  New Zealand\n",
              "11  2019                England & Wales      England  New Zealand\n",
              "12  2023                          India    Australia        India"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c58a39b0-4edd-4f9c-b9ae-3b02fa578459\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Year</th>\n",
              "      <th>Host</th>\n",
              "      <th>Winner</th>\n",
              "      <th>Runner_Up</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1975</td>\n",
              "      <td>England</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1979</td>\n",
              "      <td>England</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1983</td>\n",
              "      <td>England</td>\n",
              "      <td>India</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1987</td>\n",
              "      <td>India &amp; Pakistan</td>\n",
              "      <td>Australia</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1992</td>\n",
              "      <td>Australia &amp; New Zealand</td>\n",
              "      <td>Pakistan</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>1996</td>\n",
              "      <td>India, Pakistan &amp; Sri Lanka</td>\n",
              "      <td>Sri Lanka</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>1999</td>\n",
              "      <td>England</td>\n",
              "      <td>Australia</td>\n",
              "      <td>Pakistan</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2003</td>\n",
              "      <td>South Africa</td>\n",
              "      <td>Australia</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>2007</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>Australia</td>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>2011</td>\n",
              "      <td>India, Sri Lanka &amp; Bangladesh</td>\n",
              "      <td>India</td>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>2015</td>\n",
              "      <td>Australia &amp; New Zealand</td>\n",
              "      <td>Australia</td>\n",
              "      <td>New Zealand</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>2019</td>\n",
              "      <td>England &amp; Wales</td>\n",
              "      <td>England</td>\n",
              "      <td>New Zealand</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>2023</td>\n",
              "      <td>India</td>\n",
              "      <td>Australia</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c58a39b0-4edd-4f9c-b9ae-3b02fa578459')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-c58a39b0-4edd-4f9c-b9ae-3b02fa578459 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-c58a39b0-4edd-4f9c-b9ae-3b02fa578459');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_84138ff6-775a-4161-84ed-3d4b7634937d\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('world_cup_df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_84138ff6-775a-4161-84ed-3d4b7634937d button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('world_cup_df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "world_cup_df",
              "summary": "{\n  \"name\": \"world_cup_df\",\n  \"rows\": 13,\n  \"fields\": [\n    {\n      \"column\": \"Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15,\n        \"min\": 1975,\n        \"max\": 2023,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          2019,\n          2011,\n          1975\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Host\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 9,\n        \"samples\": [\n          \"England & Wales\",\n          \"India & Pakistan\",\n          \"West Indies\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Winner\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"West Indies\",\n          \"India\",\n          \"England\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Runner_Up\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Australia\",\n          \"England\",\n          \"Sri Lanka\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "world_cup_df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "_PnCZFD3jJXk",
        "outputId": "6591673d-5f19-4dcc-d8b7-d6c6ad7574f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Year                     Host       Winner    Runner_Up\n",
              "0  1975                  England  West Indies    Australia\n",
              "1  1979                  England  West Indies      England\n",
              "2  1983                  England        India  West Indies\n",
              "3  1987         India & Pakistan    Australia      England\n",
              "4  1992  Australia & New Zealand     Pakistan      England"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e6207af7-555b-4e6a-b0e9-fb7c2c437799\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Year</th>\n",
              "      <th>Host</th>\n",
              "      <th>Winner</th>\n",
              "      <th>Runner_Up</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1975</td>\n",
              "      <td>England</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1979</td>\n",
              "      <td>England</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1983</td>\n",
              "      <td>England</td>\n",
              "      <td>India</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1987</td>\n",
              "      <td>India &amp; Pakistan</td>\n",
              "      <td>Australia</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1992</td>\n",
              "      <td>Australia &amp; New Zealand</td>\n",
              "      <td>Pakistan</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e6207af7-555b-4e6a-b0e9-fb7c2c437799')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-e6207af7-555b-4e6a-b0e9-fb7c2c437799 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-e6207af7-555b-4e6a-b0e9-fb7c2c437799');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "world_cup_df",
              "summary": "{\n  \"name\": \"world_cup_df\",\n  \"rows\": 13,\n  \"fields\": [\n    {\n      \"column\": \"Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15,\n        \"min\": 1975,\n        \"max\": 2023,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          2019,\n          2011,\n          1975\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Host\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 9,\n        \"samples\": [\n          \"England & Wales\",\n          \"India & Pakistan\",\n          \"West Indies\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Winner\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"West Indies\",\n          \"India\",\n          \"England\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Runner_Up\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Australia\",\n          \"England\",\n          \"Sri Lanka\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "world_cup_df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IDbJKRnUjQNV",
        "outputId": "66eb0428-6881-4af4-dc94-6698bf28822f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(13, 4)"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "title_count = world_cup_df[\"Winner\"].value_counts()\n",
        "\n",
        "print(title_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qVkJGqm-jXjZ",
        "outputId": "5b7d6a4e-dc92-4d65-9bc1-f4c0f4539c49"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Winner\n",
            "Australia      6\n",
            "West Indies    2\n",
            "India          2\n",
            "Pakistan       1\n",
            "Sri Lanka      1\n",
            "England        1\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 6))\n",
        "\n",
        "title_count.plot(kind=\"bar\")\n",
        "\n",
        "plt.title(\"ICC Men's Cricket World Cup Titles\")\n",
        "plt.xlabel(\"Team\")\n",
        "plt.ylabel(\"Number of Titles\")\n",
        "\n",
        "plt.xticks(rotation=45)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 616
        },
        "id": "IjE94LhFjjmu",
        "outputId": "dee5e07c-00e0-42a0-c861-f684e617de19"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0EAAAJXCAYAAABVBV/rAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAZZFJREFUeJzt3Wd0VNX79vFrkpDQktBL6E1CBwGRjoIK0hFQugiISBOwgEpTEVApIoIUKSoIFrBQRYr8ICBF6b0jvSaEEiC5nxc8mT8xIIkmGcj5ftbK0tlnT+aemcNkrrPP3sdlZiYAAAAAcAgvTxcAAAAAAEmJEAQAAADAUQhBAAAAAByFEAQAAADAUQhBAAAAAByFEAQAAADAUQhBAAAAAByFEAQAAADAUQhBAAAAAByFEAQAiLdDhw7J5XJp2rRp8brfoEGD5HK5dPbs2cQp7D5Xo0YN1ahR4579VqxYIZfLpRUrViR6TZ6UN29ePf/883HqG9fXDgDighAE4L4zbdo0uVwubdiwIda2TZs2qXXr1sqVK5f8/PyUIUMG1apVS1OnTlVkZGSMvteuXdOoUaNUoUIFBQYGKmXKlHrooYfUrVs37dmz5x9riP4S6nK59NVXX92xT+XKleVyuVS8ePF//2TjIDpwJOQX4vi8jverK1euaNCgQXF6XdatWyeXy6VRo0bF2tawYUO5XC5NnTo11rZq1aopR44cCVFuotq/f786d+6s/PnzK2XKlAoICFDlypX18ccf6+rVq0lWx+3/bu71cyc7duzQoEGDdOjQoSSrGYAz+Xi6AACIq8mTJ+ull15S1qxZ1aZNGxUqVEiXLl3S0qVL1aFDB504cUJvvvmmJOns2bOqXbu2Nm7cqHr16qlly5ZKmzatdu/erVmzZmnixIm6fv36PR8zZcqUmjlzplq3bh2j/dChQwoJCVHKlCkT5bkmpvi8jneTJ08eXb16VSlSpEiiqmO7cuWKBg8eLEn3HCF4+OGHlTp1aq1atUq9evWKsS0kJEQ+Pj5avXq12rdv726/fv261q9fr/r16yd47Qlp/vz5atasmfz8/NS2bVsVL15c169f16pVq/Taa69p+/btmjhxYpLUUqRIEX355Zcx2vr166e0adPqrbfeitV/9+7d8vL6v+OxO3bs0ODBg1WjRg3lzZs3scsF4GCEIAAPhLVr1+qll15SxYoVtWDBAvn7+7u3vfLKK9qwYYO2bdvmbnv++ef1559/6rvvvtMzzzwT43e9++67d/xCdidPP/20fvrpJ509e1aZMmVyt8+cOVNZs2ZVoUKFdOHChf/47JJOfF/Hv7t586aioqLk6+v7QAVAHx8fVahQQatXr47Rvnv3bp09e1YtW7bUqlWrYmzbuHGjrl27pipVqvznx79y5YpSp079n3/P3x08eFDPPfec8uTJo2XLlil79uzubV27dtW+ffs0f/78BH/cu8maNWusAwbDhg1TpkyZYrVLkp+fX1KVBgAxcDocgAfC4MGD5XK5NGPGjBhf3KOVK1fOPbfg999/1/z589WhQ4dYAUi69cXro48+itPjNmzYUH5+fvr2229jtM+cOVPNmzeXt7f3He/31VdfqWzZskqVKpUyZMig5557TkePHo3Rp0aNGipevLh27Nihxx57TKlTp1aOHDn0wQcf3LOukydPqn379sqZM6f8/PyUPXt2NWzY8J6nEcXndYw+De+jjz7S6NGjVaBAAfn5+WnHjh13nRO0a9cuNW/eXJkzZ1aqVKlUuHDhewbOw4cPq2DBgipevLhOnTolSbp48aJeeeUV9+l6BQsW1PDhwxUVFeWuLXPmzDGek8vl0qBBg+76OFWqVNGpU6e0b98+d9vq1asVEBCgF1980R2Ibt8Wfb9o48aNU7FixeTn56egoCB17dpVFy9ejPE40e/rxo0bVa1aNaVOnfofR9b++usvNWrUSGnSpFGWLFnUq1cvRURE/ONrFu2DDz5QeHi4Pv/88xgBKFrBggXVs2dPSf88j+vvr1303K3o9zMgIEAZM2ZUz549de3atTjVFhe3zwmaNm2amjVrJkl67LHH3O/pP53uGBERoYEDB6pgwYLy8/NTrly59Prrr8d6/ZYsWaIqVaooXbp0Sps2rQoXLnzP0U4AyRsjQQDue1euXNHSpUtVrVo15c6d+579f/rpJ0lSmzZt/vNjp06dWg0bNtTXX3+tLl26SJI2b96s7du3a/LkydqyZUus+wwZMkT9+/dX8+bN1bFjR505c0affPKJqlWrpj///FPp0qVz971w4YJq166tJk2aqHnz5vruu+/0xhtvqESJEqpTp85d63rmmWe0fft2de/eXXnz5tXp06e1ZMkSHTly5K6nEcX3dYw2depUXbt2TS+++KJ7/lB0GLndli1bVLVqVaVIkUIvvvii8ubNq/379+vnn3/WkCFD7vi79+/fr8cff1wZMmTQkiVLlClTJl25ckXVq1fXsWPH1LlzZ+XOnVshISHq16+fTpw4odGjRytz5swaP368unTposaNG6tJkyaSpJIlS971eUSHmVWrVqlgwYKSbgWdRx99VBUqVFCKFCkUEhKiBg0auLf5+/urVKlSkm4Fg8GDB6tWrVrq0qWLdu/erfHjx2v9+vVavXp1jFMDz507pzp16ui5555T69atlTVr1jvWdPXqVdWsWVNHjhxRjx49FBQUpC+//FLLli2719siSfr555+VP39+VapUKU7946t58+bKmzevhg4dqrVr12rMmDG6cOGCvvjiiwR/rGrVqqlHjx4aM2aM3nzzTRUpUkSS3P/9u6ioKDVo0ECrVq3Siy++qCJFimjr1q0aNWqU9uzZox9++EGStH37dtWrV08lS5bUO++8Iz8/P+3bty/WqCAAhzEAuM9MnTrVJNn69evNzGzz5s0myXr27Bmn+zdu3Ngk2YULF/51DcuXLzdJ9u2339q8efPM5XLZkSNHzMzstddes/z585uZWfXq1a1YsWLu+x06dMi8vb1tyJAhMX7f1q1bzcfHJ0Z79erVTZJ98cUX7raIiAjLli2bPfPMM3et7cKFCybJPvzww3g9p/i+jgcPHjRJFhAQYKdPn77jtqlTp7rbqlWrZv7+/nb48OEYfaOiotz/P3DgQJNkZ86csZ07d1pQUJCVL1/ezp8/7+7z7rvvWpo0aWzPnj0xfk/fvn3N29vb/T6cOXPGJNnAgQPj9HzCwsLM29vbOnTo4G4rXLiwDR482MzMHnnkEXvttdfc2zJnzmxPPPGEmZmdPn3afH197cknn7TIyEh3n7Fjx5okmzJlirst+n397LPPYtVQvXp1q169uvv26NGjTZJ988037rbLly9bwYIFTZItX778rs8nNDTUJFnDhg3j9Pzv9J5F+/vrGP0+NWjQIEa/l19+2STZ5s2b4/SYZmbFihWL8ZxvlydPHmvXrp379rfffnvX5/331+7LL780Ly8v+9///hej32effWaSbPXq1WZmNmrUKPc+BwDROB0OwH0vLCxMku54+lZC9L+XJ598UhkyZNCsWbNkZpo1a5ZatGhxx75z5sxRVFSUmjdvrrNnz7p/smXLpkKFCmn5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PaQMGTKoePHi95yXVKVKFX355ZeSFGMkKPr1+frrr939omXOnFn9+vXT4MGDVbt2bTVo0EC7d+/WuHHjVL58+TteCDQuOnXqpLFjx6pt27bauHGjsmfPri+//DLOF1YtUKCAZs6cqWeffVZFihRR27ZtVbx4cV2/fl0hISH69ttv3dfhkaSOHTtq2LBh6tixo8qVK6eVK1dqz549d/39Bw8eVIMGDVS7dm2tWbNGX331lVq2bOleNjyhlS5dWt7e3ho+fLhCQ0Pl5+enxx9/XFmyZInVt02bNvrmm2/00ksvafny5apcubIiIyO1a9cuffPNN1q8eLHKlSund955RytXrlTdunWVJ08enT59WuPGjVPOnDkT5EK4AB5QHlqVDgDu6u9LZN9u48aN1rJlSwsKCrIUKVJY+vTprWbNmjZ9+vQYSxebmV25csU++ugjK1++vKVNm9Z8fX2tUKFC1r17d9u3b98/1nD7Etn/5O9LZEf7/vvvrUqVKpYmTRpLkyaNBQcHW9euXW337t33vG+7du0sT548d33Ms2fPWteuXS04ONjSpEljgYGBVqFChRjLLN9LXF7H6CWV77QU992WW962bZs1btzY0qVLZylTprTChQtb//793dtvXyI72pUrV6x69eqWNm1aW7t2rZmZXbp0yfr162cFCxY0X19fy5Qpk1WqVMk++ugju379uvu+ISEhVrZsWfP19Y3zctkTJkwwSZYjR45Y2/744w+TZJLs1KlTsbaPHTvWgoODLUWKFJY1a1br0qVLrKXY7/a+Rm/7+3LRhw8ftgYNGljq1KktU6ZM1rNnT1u0aNE9l8i+3Z49e6xTp06WN29e8/X1NX9/f6tcubJ98skndu3aNXe/K1euWIcOHSwwMND8/f2tefPmdvr06bsukb1jxw5r2rSp+fv7W/r06a1bt2529erVONUULT5LZJuZTZo0yfLnz2/e3t4xXoM7vXbXr1+34cOHW7FixczPz8/Sp09vZcuWtcGDB1toaKiZmS1dutQaNmxoQUFB5uvra0FBQdaiRYtYS7ADcBaX2T1m3wIAAEeJvjDsmTNnlClTJk+XAwAJjjlBAAAAAByFEAQAAADAUQhBAAAAAByFOUEAAAAAHIWRIAAAAACOQggCAAAA4CgP9MVSo6KidPz4cfn7+8vlcnm6HAAAAAAeYma6dOmSgoKC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24svvmhLlixxt/Xq1cuKFCliH3zwgftg2sWLF+3ixYvJegQoGiEombt586Z99dVXdwxCTZs2tSeffNIuXLjg2SKRqKZNm2ZVq1Z1f0m+ePGitWrVykqWLOkOQuHh4fbUU09Zjhw57Msvv7RJkyZZt27dzN/fn1Mk7zO3n9ry008/WUBAgGXMmNEmTJjgPs87OghVrVqVAOsgtx+tvf0c/i1bttg777xjN27csGPHjln+/Pmte/fudurUKcuePbvVqVPHQkJCku3RXqeKfj+3bNli8+bNsz///NN9ICz61LhnnnnGQkJC3PPEbty4wTywZOi7776zLFmyWN68ee1///tfjG29evWyYsWK2QcffGAnTpyIse32UaTkiBCUTER/2G3cuNEmTpxoX3zxha1bt87MYgeh6KPBu3btsuPHj3usZiS+qKgomzRpkpUvX94aN27sDkJ//vmntW/f3ipVqmSff/65md1aEKFFixZWvHhxK168uDVs2NA2b97syfJxFz///LN5e3vb8OHDbfDgwfbss89aihQpbPz48e4gdOjQIUufPr3Vrl072U5qRWy3j/YtXrzYvv32W4uMjHSP7rRp08Zatmzpnkv21FNPmcvlsurVq7tHjJF8fPvtt5Y5c2bLli2bBQcHW9euXd1zO6NHhNq2bWtr1671cKVIbO3atTNfX197//33YwXdV1991TJnzmxfffWVh6rzDEJQMhAdgL7//nvLli2bVahQwSpXrmzBwcE2d+5cM/u/IFS9enWrWLEiE9wd5Pr16zZz5kyrUaOGPf300+4gtGXLFmvTpo1VrFjRpkyZ4u7/119/WXh4OBfLvU9du3bNatWqZS+//HKM9tdee81SpEhhEyZMcL/Hhw8fZrVHB7l48aJlzZrV+vfvbz/99JO5XC774Ycf3Ntv3Lhh1atXtw8//NDd1qtXL1u3bp3t37/fEyUjER07dsyeeuop+/zzz+3IkSP2/vvvW+XKle25555zfwdYtmyZBQQEWKdOnQjBycQ/jd60aNHCgoOD7Ysvvoj1N37MmDGOO2BGCEomfvvtN8ucObONHz/ezG4tl5sqVSpLkyaNO9nfvHnTPv/8c6tdu7YdPnzYk+UiiUSfy7t161YbPHiwpU+f3po1axYjCLVt29YqVqxokyZN8mSpiIOoqCi7ceOGVa5c2QYOHGhmMecINWrU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TJmiefPmKX/+/B5+BvgvvLy8dODAAX366ac6derUXft5e3urQIECWrJkiRYsWKABAwZoxYoVatSokbJkyZKEFSOxeHnd+sr+5ptvqn379goMDNTly5f12GOPad26dUqbNq3q1aunjz76SOvWrdMTTzwR63f4+Pgkddn3N0+nMMQWfcRv9erVtnDhQjt//rxFRUXZzJkzLVeuXLEmSu/du9fMjKM9DvHHH3+Yy+Wy5s2bu0f+zp07Zz169DAfHx+bN2+emf3ffhQVFWWjR49mWdwHzO0jQnv27LFt27ZZ7dq17ciRI54uDUlg6dKl7v+/du2aXbt2zcqUKWNTp051t+/du9cqVqxoBQoUcI8ILV++3Hr27OmeO4QH35AhQyxNmjT20Ucf/ePf+e+++85q1apl2bJls4ceeoh5n8nQpEmTLE2aNLZmzRo7ffq0/f7779agQQMLCAiIsSz61KlTrXHjxix+cA+EoPtM9BfX77//3tKlS2cDBgxwr+xx+fLlGEOdV65csf79+1u5cuW46JnDrF+/3jJmzGhNmjRxB6GLFy9a165dLUWKFLGCEB5Me/bssaefftoeeeQR27t3r12/ft3TJSEJbNy40Vwul/Xq1StGe5kyZWzOnDkx2qKDUOHChe3YsWNmxoWPk6MBAwZY7ty5bfjw4f8YhPbt22eHDh3ioGgy9cYbb1iTJk1itB0+fNhq1aplGTNmdJ8aFx4ezipwcUAIug8tXbrU/P39berUqTHO8za79aV27ty5ljVrVsuTJ49lzZrVnf7hLOvWrbtrEEqdOnWsL0t4MO3cudOaNGlihw8f9nQpSCLnz5+3Tz75xLJkyWKvvvqqu71UqVK2ePFiM7MYgXjv3r0WHBxspUuXtps3b3LwIxm5fTn0t956665B6OrVq/bWW2+xGmAy9+abb1quXLlizQ+eOnWquVwuy5Ahg23dutW9jc+Cf8bqcPehfv366dChQ/r666915coVbdq0SVOnTlVAQIBq166tJ554QsePH9fatWtVrlw55c6d29Mlw0PWr1+vOnXqqHr16u59JDQ0VD179tSCBQt08OBBpUmTxtNl4j+6fv26fH19PV0GklBoaKhmzJih/v37q127dho5cqSKFy+uTz75RI899liMvpGRkTp27Jh7DikebPa3FV6j53hK0ttvv60vv/xSXbt2Vfv27ZU5c2Zdv35dr776qsaOHavNmzerRIkSniodCeT29/x2a9as0csvv6wGDRqoT58+CggIkCQtX75cs2fP1oULF7Rz506tWLFCGTJkSOqyHziEoPvA7R94N27cULdu3bRt2zYNGDBA06ZN04ULF3ThwgVlyJBB165d09dff61s2bJ5uGp4wp0+GG8PQtOmTZO/v7/CwsJ05coV9hPgAXbx4kXNnDlTb7/9tpo3b64NGzbI399fhQoV0tWrV93L3ObIkUNDhgzxcLX4r2bMmBHjEhi3u/2zv3///po+fbq6deumli1bauTIkfrss8+0evVqlSlTJilLRiK4/Tvh119/rb/++ks5cuRQixYtZGZ6++23tWLFCj3yyCPq3bu3IiMj1aNHD+XKlUv169fXCy+8oO+//16VKlXy8DO5/7E63H0getWf1atXK0WKFOrRo4dOnz6tTp06ycvLS926ddPvv/+u9u3bKywsTKlSpfJ0yUhE0Sv8RUVFuVcJPHDggCTd8chQ+fLltXDhQoWEhKhJkya6dOmSAgICCEDAAy5dunRq3ry53nvvPS1evFibN2/WY489Jl9fX3l7eytFihTy8vJyrxqKB9eOHTv0+uuv68iRI+62249Re3l5uf82vPvuu2rXrp0+++wz1a9fXxMnTtSqVasIQMlAVFSUOwC99dZb6tChg3766Se1bt1aLVq00PHjx/XOO+/o6aefVkhIiPLmzasnn3xShw4d0rhx4xQcHKzUqVMrRYoUHn4mDwhPnYeH/3Pt2jVr2bKluVwuW7lypZmZnTlzJtbqPn379rVq1aqxCIID7N692/r162dmZrNnz7Y8efLcc7WnkJAQy58/vx09ejQpSgSQgKLP3d+2bZstWLDA5s2b554TeurUKRs/frzlyJHDBg8e7MkykUgiIyPdczs3bdrkbv/7nI7bJ7n37dvXMmXKZJs3b06aIpFkdu/ebU888YStX7/ezG4tlpIlSxZr3Lixe37o5cuX7eeff7aQkBD3ftG7d28rXbo0C2PEESHIg27/cDt8+LC1a9fOfH197X//+1+MfsuXL7c33njDAgICYnw4IvmaN2+euVwua9CggblcLps2bVqc7nf7RXQBPBii/xbMmTPH8uXLZ4UKFbLSpUtbmTJl7OzZs2Zmdvr0afv0008tc+bM1qFDh1j3xYPr9vfwzJkzlj59envm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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "runner_up_count = world_cup_df[\"Runner_Up\"].value_counts()\n",
        "\n",
        "print(runner_up_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8OptzynNj5Fj",
        "outputId": "a94590ab-8a1c-44f2-aec5-99e63a79a5fb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Runner_Up\n",
            "England        3\n",
            "Australia      2\n",
            "India          2\n",
            "New Zealand    2\n",
            "Sri Lanka      2\n",
            "West Indies    1\n",
            "Pakistan       1\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "world_cup_df[\"Runner_Up\"]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 491
        },
        "id": "iN9yaU3Sj8FB",
        "outputId": "113add5b-8f62-4370-a91c-31040e531bc1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       Australia\n",
              "1         England\n",
              "2     West Indies\n",
              "3         England\n",
              "4         England\n",
              "5       Australia\n",
              "6        Pakistan\n",
              "7           India\n",
              "8       Sri Lanka\n",
              "9       Sri Lanka\n",
              "10    New Zealand\n",
              "11    New Zealand\n",
              "12          India\n",
              "Name: Runner_Up, dtype: object"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Runner_Up</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Pakistan</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>New Zealand</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>New Zealand</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> object</label>"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "runner_up_count = world_cup_df[\"Runner_Up\"].value_counts()\n",
        "\n",
        "print(runner_up_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IKhf6PMLkLah",
        "outputId": "a3dbc923-e4c3-4085-98a8-8982b647cef8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Runner_Up\n",
            "England        3\n",
            "Australia      2\n",
            "India          2\n",
            "New Zealand    2\n",
            "Sri Lanka      2\n",
            "West Indies    1\n",
            "Pakistan       1\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 6))\n",
        "\n",
        "runner_up_count.plot(kind=\"bar\")\n",
        "\n",
        "plt.title(\"ICC Men's Cricket World Cup Runner-Ups\")\n",
        "plt.xlabel(\"Team\")\n",
        "plt.ylabel(\"Number of Runner-Up Finishes\")\n",
        "\n",
        "plt.xticks(rotation=45)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 625
        },
        "id": "W4isSuMllGy3",
        "outputId": "78ad3a5a-78af-4254-a146-01240a974d17"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA04AAAJgCAYAAAC9cTNzAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAfc1JREFUeJzt3XmcjeX/x/H3mRnGNiP7vgxjyb4kjLUoZE2WL8ouFRFSKEp9hYSSJRJSiQoViWRJjLJk3/d97Axjn/n8/vCb83UynDk1M2fMvJ6Pxzw4133f53zOueecOe/7uu7rdpiZCQAAAABwTz7eLgAAAAAAEjuCEwAAAAC4QXACAAAAADcITgAAAADgBsEJAAAAANwgOAEAAACAGwQnAAAAAHCD4AQAAAAAbhCcAAAAAMANghMAJHMHDx6Uw+HQtGnTPNru7bfflsPh0JkzZ+KnsESuZs2aqlmzptv1li9fLofDoeXLl8d7TQCA+ENwAhCvpk2bJofDoXXr1t21bOPGjXr22WeVJ08e+fv7K2PGjKpdu7amTp2qyMhIl3WvXbum0aNHq2LFikqfPr1SpUqlwoULq3v37tq9e/d9a4j+4upwOPTll1/GuE6VKlXkcDhUokSJf/5kYyE6pMTll2hPXsfE6sqVK3r77bdj9bqsWbNGDodDo0ePvmtZ48aN5XA4NHXq1LuWVa9eXbly5YqLcuPVvn371LVrVxUoUECpUqVSYGCgqlSpoo8++khXr15N8Hrat2/vfP84HA75+/urcOHCGjRokK5du5bg9SS0+32GSVKDBg2UP3/+hC0KgFf4ebsAAMnT5MmT9cILLyhbtmx67rnnVKhQIV26dElLlixRp06ddOLECQ0YMECSdObMGdWtW1fr169XgwYN1Lp1a6VLl067du3SzJkzNWnSJN24ccPtY6ZKlUozZszQs88+69J+8OBBhYaGKlWqVPHyXOOTJ6/jveTLl09Xr15VihQpEqjqu125ckWDBw+WJLe9OOXKlVOaNGm0cuVK9erVy2VZaGio/Pz8tGrVKnXo0MHZfuPGDa1du1YNGzaM89rj0k8//aTmzZvL399fbdu2VYkSJXTjxg2tXLlSffv21bZt2zRp0qQEr8vf31+TJ0+WJF28eFE//PCD3n33Xe3bt09fffVVgtcDAN5AcAKQ4P744w+98MILqly5shYsWKCAgADnsldeeUXr1q3T1q1bnW3t27fXhg0b9N133+mZZ55xua93331Xb7zxRqwe96mnntKPP/6oM2fOKHPmzM72GTNmKFu2bCpUqJDOnz//L59dwvH0dfy7W7duKSoqSilTpnygQqOfn58qVqyoVatWubTv2rVLZ86cUevWrbVy5UqXZevXr9e1a9dUtWrVf/34V65cUZo0af71/fzdgQMH9J///Ef58uXT0qVLlSNHDueybt26ae/evfrpp5/i/HFjw8/Pz+WAw0svvaSQkBB9/fXXGjVqlLJly+aVuuLKne8FALgXhuoBSHCDBw+Ww+HQV1995fJlP9ojjzyi9u3bS5L+/PNP/fTTT+rUqdNdoUm6fST8gw8+iNXjNm7cWP7+/vr2229d2mfMmKEWLVrI19c3xu2+/PJLlS9fXqlTp1bGjBn1n//8R0eOHHFZp2bNmipRooS2b9+uxx57TGnSpFGuXLn0/vvvu60rLCxMHTp0UO7cueXv768cOXKocePGOnjw4H238+R1jB4i+MEHH+jDDz9UwYIF5e/vr+3bt9/zHKedO3eqRYsWypIli1KnTq0iRYq4DamHDh1ScHCwSpQooZMnT0qSLly4oFdeecU5lDA4OFjDhw9XVFSUs7YsWbK4PCeHw6G33377no9TtWpVnTx5Unv37nW2rVq1SoGBgXr++eedIerOZdHbRRs/fryKFy8uf39/5cyZU926ddOFCxdcHid6v65fv17Vq1dXmjRp7tuDd/ToUTVp0kRp06ZV1qxZ1atXL12/fv2+r1m0999/X5cvX9Znn33mEpqiBQcHq2fPnpLuf17a31+76HPRovdnYGCgMmXKpJ49e/7joXYOh0NVq1aVmWn//v33fOxo+fPnd/4uSv8b/rZq1Sr17t1bWbJkUdq0afX000/r9OnTd23boEEDrVy5Uo8++qhSpUqlAgUKaPr06Xc9jrvfNen+74W4cOf9jx49Wvny5VPq1KlVo0aNuw5k/NP3PgDvoMcJQIK6cuWKlixZourVqytv3rxu1//xxx8lSc8999y/fuw0adKocePG+vrrr/Xiiy9KkjZt2qRt27Zp8uTJ2rx5813bDBkyRAMHDlSLFi3UuXNnnT59Wh9//LGqV6+uDRs26KGHHnKue/78edWtW1dNmzZVixYt9N133+n1119XyZIlVa9evXvW9cwzz2jb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ly5V2bJlY9zG09cx2r/9ohuTZ555Rp9//rm++uorde3a1WVZVFSUnnjiCb322msxblu4cOF//LjRwWnVqlUKDQ1VyZIlnfskJCRE169f19q1a7Vy5Ur5+fk5Q5Wn4uM1+7vAwEDlzJnzvrMg3ulevTyeXLfLk54iX19f1a5d23m7Tp06Klq0qLp27eo8D/F+7lVXbN8zsVnP09+1v+/Xv0/IMXXqVLVv39454+S9rqF15cqVfzwr5T957wPwHoITgASVJk0aPf7441q6dKmOHDmiPHny3Hf9hg0baujQofryyy/jLDhVrVpVefPm1fLlyzV8+PB7rlewYEGZmYKCgv7VF/zYKFiwoPr06aM+ffpoz549KlOmjEaOHHnPC/Z6+jp6okCBApIU6y/xI0aMkJ+fn1566SUFBAS49OAVLFhQly9fdvnSHZN/MtzrzgkiVq9erSpVqjiX5cyZU/ny5dOqVau0atUqlS1b1jmFeL58+STdnr48+rlKt6/1dODAAbe13ku+fPm0detWmZnL89m1a1estm/QoIEmTZqk1atXq3LlyvddN7pn5u+zAP69t+xOe/bscell2bt3r6Kiov7RJAQ5cuRQr169NHjwYP3xxx/OUJohQ4a7arpx44ZOnDjh8WN4Kra/a/eyePFil9vRk07c+fsS02fQ7t27Y+yd3bNnT4zr/v319vS9D8B7OMcJQIJ76623ZGZ67rnndPny5buWr1+/Xp9//rkkqXLlyqpbt64mT56s77///q51b9y4oVdffdWjx3c4HBozZozeeuut+87W17RpU/n6+mrw4MF3HQE3M509e9ajx43JlStX7poSumDBggoICHA7jbUnr6MnsmTJourVq2vKlCk6fPiwy7KYes8cDocmTZqkZs2aqV27di49EC1atNDq1au1aNGiu7a7cOGCbt26JUnOUPP3L933kzNnTgUFBWnJkiVat27dXbPRhYSE6Pvvv9euXbtcpiGvXbu2UqZMqTFjxrg8n88++0wXL15U/fr1Y13DnZ566ikdP35c3333nbPtypUrsb5g7Wuvvaa0adOqc+fOzqnc77Rv3z599NFHkm73UGXOnPmu83bGjx9/z/sfN26cy+2PP/5Yku474+P9vPzyy0qTJo2GDRvmbCtYsOBdNU2aNMmjnrB/Kra/a/dSu3Ztl5/oHqjy5csra9asmjx58l3vye+//17Hjh2L8TWMXhZtzZo1+vPPP53r/pv3PgDvoMcJQIILCQnRuHHj9NJLL6lo0aJ67rnnVKhQIV26dEnLly/Xjz/+qP/+97/O9adPn64nn3xSTZs2VcOGDVWrVi2lTZtWe/bs0cyZM3XixIlYX8spWuPGjdW4ceP7rlOwYEH997//Vf/+/XXw4EE1adJEAQEBOnDggObOnavnn3/e49D2d7t371atWrXUokULFStWTH5+fpo7d65Onjyp//znP/fd1tPX0RNjxoxR1apVVa5cOT3//PMKCgrSwYMH9dNPP2njxo13re/j46Mvv/xSTZo0UYsWLbRgwQI9/vjj6tu3r3788Uc1aNDAOX10RESEtmzZou+++04HDx5U5syZlTp1ahUrVkyzZs1S4cKFlTFjRpUoUcLteVZVq1bVF198IUkuPU7Rr8/XX3/tXC9alixZ1L9/fw0ePFh169ZVo0aNtGvXLo0fP14VKlRwmeDDE126dNHYsWPVtm1brV+/Xjly5NAXX3wR64vlFixYUDNmzFDLli318MMPq23btipRooRu3Lih0NBQffvtty7XQurcubOGDRumzp0765FHHtGKFSu0e/fue97/gQMH1KhRI9WtW1erV6/Wl19+qdatWzunaPdUpkyZ1KFDB40fP147duzQww8/rM6dO+uFF17QM888oyeeeEKbNm3SokWLXC44HV9i+7vmqZQpU+qDDz5Qu3btVKFCBbVs2VKZMmXShg0bNGXKFJUqVSrGCUCCg4NVtWpVvfjii7p+/bo+/PBDZcqUyTmU8N+89wF4iVfm8gOQbNxvKt/169db69atLWfOnJYiRQrLkCGD1apVyz7//HOXaaLNzK5cuWIffPCBVahQwdKlS2cpU6a0QoUK2csvv2x79+69bw13Tkd+P3+fjjza7NmzrWrVqpY2bVpLmzatFS1a1Lp162a7du1yu227du1cpir+uzNnzli3bt2saNGiljZtWkufPr1VrFjRZUprd2LzOkZPkRzT1Mf3mtp669at9vTTT9tDDz1kqVKlsiJFitjAgQOdy++cjjzalStXrEaNGpYuXTr7448/zMzs0qVL1r9/fwsODraUKVNa5syZLSQkxD744AO7ceOGc9vQ0FArX768pUyZMtZTk0+cONEkWa5cue5a9tdff5kkk2QnT568a/nYsWOtaNGi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tGl66623NH/+fDkcDv3888/y87t7U4fDQXACAAAAkOTEKjgVKVJEM2fOlCT5+PhoyZIlypo1a7wWBgAAAACJRayC052ioqLiow4AAAAASLQ8Dk6StG/fPn344YfasWOHJKlYsWLq2bOnChYsGKfFAQAAAEBi4PF1nBYtWqRixYppzZo1KlWqlEqVKqU///xTxYsX1+LFi+OjRgAAAADwKo97nPr166devXpp2LBhd7W//vrreuKJJ+KsOAAAAABIDDzucdqxY4c6dep0V3vHjh21ffv2OCkKAAAAABITj4NTlixZtHHjxrvaN27cyEx7AAAAAJIkj4fqdenSRc8//7z279+vkJAQSdKqVas0fPhw9e7dO84LBAAAAABv8zg4DRw4UAEBARo5cqT69+8vScqZM6fefvtt9ejRI84LBAAAAABv8zg4ORwO9erVS7169dKlS5ckSQEBAXFeGAAAAAAkFv/oOk7RCEwAAAAAkgOPJ4cAAAAAgOSG4AQAAAAAbhCcAAAAAMANj4LTzZs3VatWLe3Zsye+6gEAAACARMej4JQiRQpt3rw5vmoBAAAAgETJ46F6zz77rD777LP4qAUAAAAAEiWPpyO/deuWpkyZol9//VXly5dX2rRpXZaPGjUqzooDAAAAgMTA4+C0detWlStXTpK0e/dul2UOhyNuqgIAAACARMTj4LRs2bL4qAMAAAAAEq1/PB353r17tWjRIl29elWSZGZxVhQAAAAAJCYeB6ezZ8+qVq1aKly4sJ566imdOHFCktSpUyf16dMnzgsEAAAAAG/zODj16tVLKVKk0OHDh5UmTRpne8uWLbVw4cI4LQ4AAAAAEgOPz3H65ZdftGjRIuXOndulvVChQjp06FCcFQYAAAAAiYXHPU4REREuPU3Rzp07J39//zgpCgAAAAASE4+DU7Vq1TR9+nTnbYfDoaioKL3//vt67LHH4rQ4AAAAAEgMPB6q9/7776tWrVpat26dbty4oddee03btm3TuXPntGrVqvioEQAAAAC8yuMepxIlSmj37t2qWrWqGjdurIiICDVt2lQbNmxQwYIF46NGAAAAAPAqj3ucJCl9+vR644034roWAAAAAEiU/lFwOn/+vD777DPt2LFDklSsWDF16NBBGTNmjNPiAAAAACAx8Hio3ooVK5Q/f36NGTNG58+f1/nz5zVmzBgF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saJ99NFHLuv95z//sY4dOzqPvvXu3dtWr15tp0+fTtB6k5uDBw/a1q1bzczs2rVrzvZTp06ZmVmXLl2sVatWzl6/Fi1aWPbs2S0kJMTCw8PpaUgiovfj/PnzrWXLllarVi2bPXu2mZkdO3bMWrRoYRUrVrRXXnnFfv75Z+vevbvlzp3bjhw54s2yk6xx48ZZgwYNbP369c62HTt2WIECBezy5cvOtjNnzljGjBmtR48edvr0aXv99detRIkSzvcvEqe5c+damjRp7M0337S3337bateubUFBQbZv3z7nOqtWrbJXXnnFHnroIdu4caMXq03epk+fbj4+PvbOO+84v59Ef17OmTPHsmTJYmFhYd4s0WMEp2Qi+hfWzFy6TCMjI+3555+3SpUq2U8//eRsP336tHXp0sVCQ0Pt1q1bCVorbtu2bZsVL17cnnjiCTt79qyzrWXLllatWjWbOHGic91evXpZhgwZ7N1337V27dpZQECA7dmzx1ulJ3l//fWXhYeHO28vW7bMQkJCXL4IX7t2zSpWrGhvvvmmmf3vvTZmzBgCbRK0dOlSS5MmjXXo0MEaNWpkvr6+9sYbb9i1a9fs+PHj9s4771jRokWtYMGCVrx4cfvrr7+8XXKStXjxYsudO7c999xztm7dOjO7PZSrePHiznVu3rxpZmZTp061VKlSWb58+Sx79uzsl0QuLCzMKleubB9//LGZ3R4KnSlTJuvVq5dznZMnT1rnzp2tVq1atnnzZm+VmqxEh6Hr16/b9evXXZaNHz/efHx8bNiwYc71ov+980DGg4LglAzceVR76NCh1qBBA6tVq5YtWrTIbty4YZs3b7bmzZtbkSJF7N1337WvvvrKateubSEhIc5to//IIOFERkbaV199ZdWrV7d69eo5j4Ju377d2rdvb5UrV7bx48c71+/QoYOVL1/eqlWrxhG2eBIVFWXLly83h8Phcv7Y/v37LWvWrFajRg07duyYmd1+z3To0MGqV69uX3zxhb366quWJ08eehmSoJMnT9qwYcNszJgxzraJEydaQECA9e/f3yVkHz169K7z4hB3ov9m/fbbbxYUFGStW7e2bdu22cqVKy04ONiuXr161zb79++3ZcuW2dGjRxO6XNzHhx9+aNOnT3dpO378uBUpUsQOHDhgBw8etNy5czvP7TUz+/nnn+3SpUt2/Phxl3OCEX+i33MLFy60Jk2aWPXq1a1jx44WFhbmXDZu3Djz8fGx999//4EfaUFwSuLu7GkaPXq0pU+f3t5++22rXLmyFShQwD744AO7fv267d692wYPHmxZs2a18uXLW61atezGjRtmFvMQP8Sv6Nc8MjLSvv76a6tSpYrVrVvXbXg6e/asXblyxSs1Jyevv/66pUqVyiZMmOD8Unzw4EErWLCgValSxRmeFi1aZI0aNbLcuXNbiRIlXIYO4cEXFRVlu3fvNofDYblz53bpBTYz++STTyxdunQ2cOBAO3TokJeqTH6i/+4tX77cgoKCrEuXLjZq1CgrXry4zZkzx7755htbuHChLV682KZOnUqvRCITGRlpx48fty5dutju3btdlu3fv985QiYoKMg6d+7s3N+7du2yDh062PLly71RdrL2/fffW2BgoHXv3t2mT59uuXLlsvr169vatWud32cmTJhgDofDPvzwQy9X++8QnJKJbdu22fPPP2+LFy92tvXq1csefvhhe//9951f/i5cuGAXLlygpykRiB4iGRkZaTNmzLhneKpWrZqNHDnSm6UmG9EHE8zM3njjDfP397fJkyc7ZwY6cOCAFSxY0CpXruw8N+3cuXN25MgRhuclYe+++645HA7r2bOnS++Smdmnn35qDofD/vvf/zLs2Qt+/fVXCwoKsty5c1tgYKCVL1/e8uXLZyVKlLCiRYtazpw5be/evd4uE3eIPl80ehhXaGioTZ482bm8RYsWMc58+Prrr1uZMmXoOUxgO3bssGLFitnYsWPNzCw8PNxy5cplqVKlsrJly9q6deuc4Xby5Mm2fft2b5b7rxGckoHvvvvOsmbNavnz57fff//dZVmvXr2sePHi9v7779uJEydclt3ZWwXvunXrln355ZcxhqdmzZrZk08+aefPn/dukcnAncOAfvzxRwsMDLRMmTLZxIkTnecORoenatWq8Qc8GXnnnXfM4XDY2LFjXc4jNbt9Hs3OnTu9VFnyEP3e3Lx5s82fP982bNjg/OIdPWzvmWeesdDQUOc5GDdv3nwgz7FIyqZNm2bVqlVzHoy6cOGCtWnTxkqVKuUMT5cvX7Y6depYrly57IsvvrBPP/3UunfvbgEBAQxTj0d3jj668yDQ5s2b7Z133rGbN2/asWPHrECBAvbyyy/byZMnLUeOHFavXj0LDQ1NMqOXCE7JRLt27SxlypT23nvv3fWH4tVXX7UsWbLYl19+6aXqEC36g2X9+vU2adIkmz59uq1Zs8bM7g5P0T0YO3futOPHj3ut5uRm3rx55uvra8OHD7fBgwdby5YtLUWKFDZhwgTnF+aDBw9ahgwZrG7duvQyJCHR789t27bZihUrbMmSJS4HmAYOHGg+Pj42duxYvpB7wbfffmtZsmSx7NmzW9GiRa1bt27O81yie57atm1rf/zxh5crRUyioqLs008/tQoVKtjTTz/tDE8bNmywDh06WEhIiH322WdmdntSiFatWlmJEiWsRIkS1rhxY9u0aZM3y08W7hw5sWjRIvv2228tMjLS2Yv03HPPWevWrZ3n/9apU8ccDofVqFHDZebZBxnBKYm5Xy9Rq1atrGjRojZ9+vS7Loo6ZswYvuB5WfSXstmzZ1v27NmtYsWKVqVKFStatKjNnTvXzP4XnmrUqGGVK1fm5NcEdu3aNatdu7a99NJLLu19+/a1FClS2MSJE51/7A8dOsTMhknInVPo5syZ00qVKmUpUqSwZ5991latWuVcb+DAgZYqVSobMWIEF59OQMeOHbM6derYZ599ZocPH7b33nvPqlSpYv/5z3+cn5NLly61wMBA69KlS5L5EpfU3Lhxw2bMmGE1a9a0p556yvl5unnzZnvuueescuXKNmXKFOf6R48etcuXL/NeSwAXLlywbNmy2cCBA+3HH380h8Nh33//vXP5zZs3rUaNGjZixAhnW69evWzNmjUuU8U/6AhOScidoen333+32bNn219//eWcytrMrHnz5vbwww/HGJ7MjPDkZb/99ptlyZLFJkyYYGa3p7lOnTq1pU2b1tkjeOvWLfvss8+sbt26nHCegKKiouzmzZtWpUoVe+utt8zM9ZynJk2aWM6cOe3jjz++a6gWHlx3fiYuXrzYMmbMaJMmTXLedjgc9vTTT9uKFSuc6/Xu3dsyZcpk586dS/B6k6N169ZZ+/btrUWLFs7XPCoqyiZMmGAhISEu4em3337jgEYiFX1O9ZYtW2zw4MGWIUMGa968uUt4atu2rVWuXNk+/fRTb5aaLN24ccO+/fZb8/f3N39/f5s5c6aZ/e+7540bN6x06dJWr149W7BggfXp0+eBvE6TOwSnJOLOsaP9+vWzXLlyWdGiRS179uzWo0cP57UszG6fWFmyZEmbMGECR90SkaioKOvfv7+9+uqrZmZ25MgRy5cvn7Vp08Y6depkadKkcR7duXXrFlMae0mHDh2saNGizmmNo8NTnz59LH369JY1a1bON0sCZsyY4ZwdMTIy0i5fvmwvv/yyvfHGG2Zmtm/fPgsODrYmTZpY7ty57bHHHnMJT1xENWFERkbagAEDLG/evFawYEGXA4i3bt2yCRMmWPXq1e2pp55yOYiIxGnmzJn28MMPW5s2baxkyZKWMWNGa9iwoTMQb9682Tp06GDFihWzL774wsvVJj+bNm0yh8NhDofDBg8e7GyPDr07duywXLlyWcGCBa1gwYJJ8rpoBKck4M6Z74YPH265cuWy3377zcxun78UEBBgzz77rPNcGTOzWrVqWZs2bZLMyXoPqujXf9myZbZ582Y7fPiwrVixwi5fvmwVK1a0zp07m9ntaXX9/PzM4XDY119/7c2Sk43ofXPs2DE7fPiwMyht3brVypUrZw0bNnQ58NCnTx9bsmQJs+clATt27LBSpUrZY4895pw05+rVq/bLL7/Ynj177Pz581auXDnr1KmTmd2+doy/v7/VqVPHOQEPn60JJyIiwoYMGWK5c+e2bt26uVyS4datWzZq1CirU6cOk7Ukcnv37rWcOXPa2LFjnRN4jBkzxh599FFr1KiRyzlPL7zwgh04cMCL1SYf0Z9lZ8+etcuXL9umTZts5syZliJFChswYIBzvejvotevX7fDhw8n2b+FBKcH2KhRo5z/v3Xrlh07dsyaNm3qPArzww8/WPr06a19+/aWJ08ea9mypa1du9a5TfSROf7Ae9fSpUstICDAvvnmG2dbaGioPfLII85rWGzdutWaNGlib7/9NrNzJaDvvvvOihcvbpkzZ7Y2bdrYzz//bGZmc+fOtbJly1rBggWtR48e1rRpU0uVKhX7JgmZNWuWPf7441a7dm3n5CvRQzBnzZplFSpUcA6VnTt3rlWqVMkeffRRLnAcz6L/XkWHo+gv2BERETZw4ECrVKmS9enTx+WgRmRkJL3AD4A//vjDsmTJ4nJdrStXrtioUaMsMDDQWrVq5ex5it7viF/R77cff/zRnn76aVu4cKHdvHnTrl+/blOmTDE/Pz978803netPnDjRvv32W2+VmyAITg+olStXmp+fn7Vu3drZdvnyZVuyZImdPXvW1q5da7lz53Ze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u3ZNqVKl8nYZQLIQHh6uwMBAXblyRf369dO1a9fUoUMH9ezZU7Vr19b8+fN15MgRhYaGcl2SRGbXrl164YUXlCFDBg0ZMoT9k0hEn9N0/vx5ZciQwdl+8eJFVa9eXdmyZdMvv/yisLAwNWzY0Dmd/9WrV7Vq1SpNmTJFK1euZHgekhV6nIB/iNAEJIzNmzercuXK+uabb5QmTRoNGjRIP/74o/MSALly5VKBAgV08eJFDR48mB6nRKZIkSKaNWuWpk6dSmhKRHx8fLRv3z4VLlxYTZo00alTp3TlyhWlT59en376qX7//XeNGDFC2bNn1zfffKOsWbOqT58+GjRokHbu3Knff/+d0IRkhxNpAACJUvQR8Vu3bql27dp67rnn9Ouvv6pr166aPXu23nvvPZUqVUrdunVTq1at9MYbb6hHjx7OoURIPLJmzertEhCDqKgo3bp1Sz/++KOuXr2qp556SrVq1dKjjz6qF198UbNmzVKNGjX06KOP6tdff9WhQ4eULl06+fv7K126dN4uH0hwDNUDACQq0TOtRUREKG3atIqMjJSvr68WLVqk0aNH69KlS8qWLZuyZcum4OBg9enTx9slAw+MOw9I+Pn5acyYMTp48KDSpEmjs2fPav369XrnnXeUKVMmPffcc2rdurUGDhzIRB6AGKoHAEhEokPTwoUL9dxzz+nxxx9XgwYNtHPnTtWpU0cTJ07UCy+8oN27d2vixInq27evdu3a5e2ygUQv+jj5lStXJP1v9t7SpUtrx44dqlKlikaNGqW2bduqVatWWrlypYKCgjR69Ght27bNa3UDiQnBCQCQaDgcDv34449q2rSpypQpo65du+r69euqUKGC9u3bp3z58um5557Tn3/+qQ4dOih37twMzQNiweFwKCwsTMWKFdMbb7yhw4cPS5Jq1KihKlWqqG3btjp37py6d++uefPmaevWrfL19dXFixc1YMAARUZG3jULH5DcMFQPAOA1f78A6uXLl9WkSRM98cQTev3113X06FFVr15dTzzxhCZOnHjX9n+fEQzAvV24cEFjxozRqFGjVL58eTVs2FCvvPKKJKl9+/aSpI8++kjp06fXyZMntX37do0cOVJDhw5VyZIlvVc4kEgQnAAACe7v5zFFn3dx5swZPfroo1q0aJEyZMigMmXKqH79+s7Q9MUXX6hJkyYKCAjw8jMAHlzbt2/XW2+9pY0bNyp37tz65JNPtHnzZv3000969tlnVbt2bee6fz+4ASRnDNUDACQ4h8OhU6dOKX/+/Prmm2/k4+MjM1PmzJlVsmRJff31184j4mPHjpUknT59WnPnztWCBQu8XD3wYCtWrJgmTpyoDz/8UBcvXtRTTz2lv/76S1u3btW3337rsi6hCfgfghMAwCt8fHzUqFEjPffcc/rhhx/kcDh08+ZNFSxYUCNHjlSxYsU0YcIEpUiRQpI0atQo7d69WyEhIV6uHHjwZcyYUfXr19dff/2lRo0aaePGjQoLC9Onn36qyZMne7s8IFFiqB4AIEHENOTn1KlTGjJkiD7++GPNnj1bTz/9tM6fP69WrVrp9OnTqlq1qgoXLqz169drzpw5Wr58ucqUKeOdJwAkMXe+J5cvX66FCxdq/PjxWrNmjYoWLerl6oDEh+AEAIh30ecwRUREKDIyUoGBgc5lJ06c0Hvvvadx48bp22+/1TPPPKOzZ89q2LBhWrt2rSIiIlS4cGH1799fJUqU8OKzAJKevx/QCA8Pd3l/AvgfghMAIEHs2bNHLVq0ULp06dSlSxdlz55dTz75pCTp+vXr6tOnj8aPH69Zs2apefPmunXrlnx8fHTz5k35+vo6rzsDAIA38FcIABDvoqKiNG3aNG3atEmpUqXShQsXdOXKFWXMmFGPPvqoOnbsqA4dOihTpkxq2bKlAgMDVadOHZmZ/P39vV0+AAD0OAEAEkZYWJiGDx+uffv2KTg4WN26ddNXX32l33//XZs3b1bGjBlVoEABrV+/XqdOndLy5ctVvXp1b5cNAIAkepwAAAkke/bs6tu3r9577z2tXLlShQoV0qBBgyRJf/75p44fP65JkyYpa9asOnXqlDJnzuzligEA+B96nAAACSp6Mog///xTTZo00YABA5zLbt68qaioKF28eFFZs2b1YpUAALgiOAEAElxYWJiGDBmitWvXqkmTJurXr58k6datW0wCAQBIlAhOAACviA5PGzZsUK1atTR48GBvlwQAwD35eLsAAEDylD17dr3xxhsqVKiQQkNDdfbsWW+XBADAPdHjBADwqpMnT0qSsmXL5uVKAAC4N4ITAAAAALjBUD0AAAAAcIPgBAAAAABuEJwAAAAAwA2CEwAAAAC4QXACAAAAADcITgAAAADgBsEJAAAAANwgOAEAAACAGwQnAMADxeFw3Pfn7bff9naJAIAkyM/bBQAA4IkTJ044/z9r1iwNGjRIu3btcralS5fOG2UBAJI4epwAAA+U7NmzO3/Sp08vh8Ph0jZz5kw9/PDDSpUqlYoWLarx48e7bP/666+rcOHCSpMmjQoUKKCBAwfq5s2bzuVvv/22ypQpoylTpihv3rxKly6dXnrpJUVGRur9999X9uzZlTVrVg0ZMiShnzoAwIvocQIAJBlfffWVBg0apLFjx6ps2bLasGGDunTporRp06pdu3aSpICAAE2bNk05c+bUli1b1KVLFwUEBOi1115z3s++ffv0888/a+HChdq3b5+aNWum/fv3q3Dhwvrtt98UGhqqjh07qnbt2qpYsaK3ni4AIAE5zMy8XQQAAP/EtGnT9Morr+jChQuSpODgYL377rtq1aqVc53//ve/WrBggUJDQ2O8jw8++EAzZ87UunXrJN3ucRoxYoTCwsIUEBAgSapbt6527dqlffv2ycfn9mCNokWLqn379urXr188PkMAQGJBjxMAIEmIiIjQvn371KlTJ3Xp0sXZfuvWLaVPn955e9asWRozZoz27duny5cv69atWwoMDHS5r/z58ztDkyRly5ZNvr6+ztAU3Xbq1Kl4fEYAgMSE4AQASBIuX74sSfr000/vGj7n6+srSVq9erXatGmjwYMHq06dOkqfPr1mzpypkSNHuqyfIkUKl9sOhyPGtqioqLh+GgCARIrgBABIErJly6acOXNq//79atOmTYzrhIaGKl++fHrjjTecbYcOHUqoEgEADzCCEwAgyRg8eLB69Oih9OnTq27durp+/brWrVun8+fPq3fv3ipUqJAOHz6smTNnqkKFCvrpp580d+5cb5cNAHgAMB05ACDJ6Ny5syZPnqypU6eqZMmSqlGjhqZNm6agoCBJUqNGjdSrVy91795dZcqUUWhoqAYOHOjlqgEADwJm1QMAAAAAN+hxAgAAAAA3CE4AAAAA4AbBCQAAAADcIDgBAAAAgBsEJwAAAABwg+AEAAAAAG4QnAAAAADADYITAAAAALhBcAIAAAAANwhOAAAAAOAGwQkAAAAA3CA4AQAAAIAb/wfoDdhwb0SiQgAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.title(...)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 470
        },
        "id": "hx9dAHQmlSmY",
        "outputId": "c26dd63a-42b8-4206-a4d7-59169d16dde3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, 'Ellipsis')"
            ]
          },
          "metadata": {},
          "execution_count": 34
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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rurqar355puhseuuu04jR45Ufn5+k+4zEAgoOjpaVVVVioqKsrNcAADQTlrj+bubnYNra2tVWlqqrKys0FhYWJg8Ho9KSkoanFNSUiKv11tvLC0tTa+//nqj91NTU6OamprQz1VVVZL+9y8AAACY4afnbZuvkZyXrXCprKxUXV2dXC5XvXGXy6UDBw40OMfn8zV4vM/na/R+cnJytHz58nPG3W63neUCAIAO4LvvvlN0dHSLnMtWuLSVrKyseq/SnDx5UpdddpnKy8tb7IGjeQKBgNxutyoqKnjbrp2xFx0He9GxsB8dR1VVlS699FL17du3xc5pK1xiYmIUHh4uv99fb9zv9ys2NrbBObGxsbaOlySn0ymn03nOeHR0NP8RdhBRUVHsRQfBXnQc7EXHwn50HGFhLfftK7bOFBERocTERBUVFYXGgsGgioqKlJqa2uCc1NTUesdL0s6dOxs9HgAAoDG23yryer2aMWOGkpKSlJycrNzcXFVXVyszM1OSlJGRoQEDBignJ0eS9NBDD+n666/X6tWrdfPNN2vLli3avXu31q9f37KPBAAAdHq2wyU9PV0nTpzQ0qVL5fP5NHLkSBUWFoYuwC0vL6/3ktCYMWP04osvavHixVq4cKGuuOIKvf766xo2bFiT79PpdCo7O7vBt4/QttiLjoO96DjYi46F/eg4WmMvbH+PCwAAQHvhdxUBAABjEC4AAMAYhAsAADAG4QIAAIxBuAAAAGN0mHDJy8tTfHy8IiMjlZKSol27dp33+FdeeUVDhw5VZGSkhg8froKCgjZaaednZy82bNig8ePHq0+fPurTp488Hs+v7h2azu6fi59s2bJFDodDU6dObd0FdiF29+LkyZOaPXu24uLi5HQ6NWTIEP6eaiF29yI3N1dXXnmlevToIbfbrXnz5unHH39so9V2Xu+//74mT56s/v37y+FwnPeXJ/+kuLhYo0ePltPp1ODBg7V582b7d2x1AFu2bLEiIiKsTZs2WZ9//rk1a9Ysq3fv3pbf72/w+A8//NAKDw+3nnzySWvfvn3W4sWLre7du1uffvppG6+887G7F9OmTbPy8vKsvXv3Wvv377fuvvtuKzo62vrmm2/aeOWdj929+MmRI0esAQMGWOPHj7duueWWtllsJ2d3L2pqaqykpCRr0qRJ1gcffGAdOXLEKi4utsrKytp45Z2P3b144YUXLKfTab3wwgvWkSNHrB07dlhxcXHWvHnz2njlnU9BQYG1aNEi69VXX7UkWa+99tp5jz98+LDVs2dPy+v1Wvv27bOefvppKzw83CosLLR1vx0iXJKTk63Zs2eHfq6rq7P69+9v5eTkNHj87bffbt188831xlJSUqy//OUvrbrOrsDuXvzS2bNnrV69elnPP/98ay2xy2jOXpw9e9YaM2aMtXHjRmvGjBmESwuxuxfPPPOMNXDgQKu2tratlthl2N2L2bNnW7///e/rjXm9Xmvs2LGtus6upinh8uijj1rXXHNNvbH09HQrLS3N1n21+1tFtbW1Ki0tlcfjCY2FhYXJ4/GopKSkwTklJSX1jpektLS0Ro9H0zRnL37p9OnTOnPmTIv+JtCuqLl78dhjj6lfv36655572mKZXUJz9uKNN95QamqqZs+eLZfLpWHDhmnlypWqq6trq2V3Ss3ZizFjxqi0tDT0dtLhw4dVUFCgSZMmtcma8bOWeu62/ZX/La2yslJ1dXWhXxnwE5fLpQMHDjQ4x+fzNXi8z+drtXV2Bc3Zi1+aP3+++vfvf85/nLCnOXvxwQcf6Nlnn1VZWVkbrLDraM5eHD58WO+++67uuusuFRQU6NChQ3rggQd05swZZWdnt8WyO6Xm7MW0adNUWVmpcePGybIsnT17Vvfdd58WLlzYFkvG/9PYc3cgENAPP/ygHj16NOk87f6KCzqPVatWacuWLXrttdcUGRnZ3svpUk6dOqXp06drw4YNiomJae/ldHnBYFD9+vXT+vXrlZiYqPT0dC1atEj5+fntvbQup7i4WCtXrtS6deu0Z88evfrqq9q+fbtWrFjR3ktDM7X7Ky4xMTEKDw+X3++vN+73+xUbG9vgnNjYWFvHo2masxc/eeqpp7Rq1Sq98847GjFiRGsus0uwuxdfffWVjh49qsmTJ4fGgsGgJKlbt246ePCgBg0a1LqL7qSa8+ciLi5O3bt3V3h4eGjsqquuks/nU21trSIiIlp1zZ1Vc/ZiyZIlmj59umbOnClJGj58uKqrq3Xvvfdq0aJF9X4pMFpXY8/dUVFRTX61ReoAr7hEREQoMTFRRUVFobFgMKiioiKlpqY2OCc1NbXe8ZK0c+fORo9H0zRnLyTpySef1IoVK1RYWKikpKS2WGqnZ3cvhg4dqk8//VRlZWWh25QpUzRx4kSVlZXJ7Xa35fI7leb8uRg7dqwOHToUikdJ+uKLLxQXF0e0XIDm7MXp06fPiZOfgtLidwy3qRZ77rZ33XDr2LJli+V0Oq3Nmzdb+/bts+69916rd+/els/nsyzLsqZPn24tWLAgdPyHH35odevWzXrqqaes/fv3W9nZ2XwcuoXY3YtVq1ZZERER1rZt26xvv/02dDt16lR7PYROw+5e/BKfKmo5dveivLzc6tWrl/Xggw9aBw8etN58802rX79+1uOPP95eD6HTsLsX2dnZVq9evayXXnrJOnz4sPX2229bgwYNsm6//fb2egidxqlTp6y9e/dae/futSRZa9assfbu3Wt9/fXXlmVZ1oIFC6zp06eHjv/p49CPPPKItX//fisvL8/cj0NblmU9/fTT1qWXXmpFRERYycnJ1scffxz6Z9dff701Y8aMese//PLL1pAhQ6yIiAjrmmuusbZv397GK+687OzFZZddZkk655adnd32C++E7P65+P8Il5Zldy8++ugjKyUlxXI6ndbAgQOtJ554wjp79mwbr7pzsrMXZ86csZYtW2YNGjTIioyMtNxut/XAAw9Y//nPf9p+4Z3Me++91+Df/z/9+58xY4Z1/fXXnzNn5MiRVkREhDVw4EDrueees32/DsvitTIAAGCGdr/GBQAAoKkIFwAAYAzCBQAAGINwAQAAxiBcAACAMQgXAABgDMIFAAAYg3ABAADGIFwAAIAxCBcAAGAMwgUAABjj/wD35O2ppI2E6AAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.xlabel(...)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 473
        },
        "id": "_5nCyFnyla8m",
        "outputId": "a5a4fa34-6c26-41a1-cdf7-e9450ec2409e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 0, 'Ellipsis')"
            ]
          },
          "metadata": {},
          "execution_count": 35
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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q6srGhoaorKystc5lZWVPcZHRDzzzDOHHQ8AcDh5v1RUW1sb8+fPj5kzZ8asWbNi+fLlsW/fvliwYEFERMybNy8mTZoU9fX1ERFx4403xsUXXxz3339/XHbZZbF27dp44YUX4uGHHx7YRwIAHPPyDpeampp49913Y9myZdHS0hLTp0+PzZs3d78Bd9euXT0uCV1wwQXx+OOPx6233ho333xznHbaabFhw4Y4++yz+3yfuVwu6urqen35iCPLXhw97MXRw14cXezH0WMw9iLv73EBABgqfqsIAEiGcAEAkiFcAIBkCBcAIBlHTbisXLkyJk+eHMXFxVFRURFbt2792PE/+clPYurUqVFcXBznnHNObNq06Qit9NiXz16sXr06LrroohgzZkyMGTMmqqqqPnHv6Lt8/158aO3atVFQUBBz5swZ3AUOI/nuxd69e2PhwoUxYcKEyOVycfrpp/v/1ADJdy+WL18eZ5xxRhx33HFRXl4eixYtij/+8Y9HaLXHrl/96lcxe/bsmDhxYhQUFHzsbxB+aMuWLfH5z38+crlcnHrqqbFmzZr87zg7CqxduzYrKirKHn300ey3v/1tdu2112ajR4/OWltbex3/3HPPZYWFhdm9996bvfzyy9mtt96ajRo1KnvppZeO8MqPPfnuxRVXXJGtXLkye/HFF7Pt27dnV111VVZaWpr993//9xFe+bEn37340Ouvv55NmjQpu+iii7K/+7u/OzKLPcbluxcHDhzIZs6cmV166aXZs88+m73++uvZli1bsubm5iO88mNPvnvxox/9KMvlctmPfvSj7PXXX8+efvrpbMKECdmiRYuO8MqPPZs2bcpuueWW7Mknn8wiIlu/fv3Hjt+5c2d2/PHHZ7W1tdnLL7+cff/7388KCwuzzZs353W/R0W4zJo1K1u4cGH3nzs7O7OJEydm9fX1vY7/2te+ll122WU9jlVUVGT/+I//OKjrHA7y3Ys/d/DgwezEE0/MHnvsscFa4rDRn704ePBgdsEFF2Q/+MEPsvnz5wuXAZLvXjz00EPZKaecknV0dBypJQ4b+e7FwoULs7/5m7/pcay2tja78MILB3Wdw01fwuU73/lO9rnPfa7HsZqamqy6ujqv+xryl4o6Ojqiqakpqqqquo+NGDEiqqqqorGxsdc5jY2NPcZHRFRXVx92PH3Tn734c/v3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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.ylabel(...)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 453
        },
        "id": "C5mSLUxdlmyr",
        "outputId": "d9252bd6-9d9a-4b07-c2d0-9f3287d70500"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0, 0.5, 'Ellipsis')"
            ]
          },
          "metadata": {},
          "execution_count": 36
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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7NixDq8ALV++XA6HQ8uXL9eXX36pH/7wh5oxY4aefPLJaD0EAADQjzmMZe8p+f1+JScnq7m5WUlJSdEeBwAAdEO4nr/71afGAAAAQokQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtaIeQuXl5crIyFBiYqJycnK0Z8+eS64/ffq0FixYoOHDh8vpdOqaa65RZWVlhKYFAACxZEA073zr1q3yeDzatGmTcnJyVFZWpvz8fB08eFBpaWmd1re1tennP/+50tLStH37do0cOVKff/65hg4dGvnhAQBAv+cwxpho3XlOTo5uvvlmbdy4UZIUCATkdru1cOFCLV26tNP6TZs26amnntKBAwc0cODAXt2n3+9XcnKympublZSU9L3mBwAAkRGu5++ovTXW1tam2tpa5eXl/WeYuDjl5eWppqamy33efvtt5ebmasGCBXK5XLrxxhu1Zs0atbe3X/R+Wltb5ff7O1wAAACkKIZQU1OT2tvb5XK5Omx3uVzyer1d7tPY2Kjt27ervb1dlZWVWrFihZ5++mk98cQTF72f0tJSJScnBy9utzukjwMAAPRfUT9ZuicCgYDS0tL0/PPPKysrSwUFBVq2bJk2bdp00X2Ki4vV3NwcvBw/fjyCEwMAgL4saidLp6amKj4+Xj6fr8N2n8+n9PT0LvcZPny4Bg4cqPj4+OC26667Tl6vV21tbUpISOi0j9PplNPpDO3wAAAgJkTtFaGEhARlZWWpuro6uC0QCKi6ulq5ubld7jN58mQdPnxYgUAguO3QoUMaPnx4lxEEAABwKVF9a8zj8Wjz5s165ZVX1NDQoAceeEAtLS2aO3euJKmwsFDFxcXB9Q888IBOnTqlRYsW6dChQ9qxY4fWrFmjBQsWROshAACAfiyq3yNUUFCgkydPauXKlfJ6vcrMzFRVVVXwBOpjx44pLu4/reZ2u/Xuu+9q8eLFGjdunEaOHKlFixZpyZIl0XoIAACgH4vq9whFA98jBABA/xNz3yMEAAAQbYQQAACwFiEEAACsRQgBAABrEUIAAMBahBAAALAWIQQAAKxFCAEAAGsRQgAAwFqEEAAAsFavQqiurk779+8PXv/zn/+smTNn6tFHH1VbW1vIhgMAAAinXoXQ/fffr0OHDkmSGhsbdeedd2rw4MHatm2bHnnkkZAOCAAAEC69CqFDhw4pMzNTkrRt2zb93//9n1577TVt2bJFf/rTn0I5HwAAQNj0KoSMMQoEApKk9957T9OmTZMkud1uNTU1hW46AACAMOpVCGVnZ+uJJ57QH/7wB/31r3/V9OnTJUlHjhyRy+UK6YAAAADh0qsQKisrU11dnR566CEtW7ZMV199tSRp+/btmjRpUkgHBAAACBeHMcaE6sbOnTun+Ph4DRw4MFQ3GXJ+v1/Jyclqbm5WUlJStMcBAADdEK7n7wEhuyVJiYmJobw5AACAsOp2CA0bNkyHDh1SamqqUlJS5HA4Lrr21KlTIRkOAAAgnLodQr/73e80ZMiQ4D9fKoQAAAD6g5CeI9QfcI4QAAD9T7iev/mJDQAAYK2Q/MRGQUEBP7EBAAD6nZD8xMbUqVP5iQ0AANDv8BMbAADAWvzEBgAAsBY/sQEAAKzFT2wAAIA+r0/+xMbevXvV0NAgSbruuuuUnZ0dkqEAAAAioVch9MUXX2jWrFn6+OOPNXToUEnS6dOnNWnSJFVUVOiKK64I5YwAAABh0atzhObNm6fz58+roaFBp06d0qlTp9TQ0KBAIKB58+aFekYAAICw6NU5QoMGDdLu3bs1YcKEDttra2s1ZcoUnT17NmQDhhrnCAEA0P/0qZ/YcLvdOn/+fKft7e3tGjFixPceCgAAIBJ6FUJPPfWUFi5cqL179wa37d27V4sWLdL69etDNhwAAEA49eqtsZSUFJ09e1YXLlzQgAH/Pt/623++7LLLOqw9depUaCYNEd4aAwCg/+lTH58vKysL2QAAAADR0qsQKioqCvUcAAAAEdftEPL7/cGXovx+/yXX8pYTAADoD7odQikpKfrqq6+UlpamoUOHyuFwdFpjjJHD4VB7e3tIhwQAAAiHbofQ+++/r2HDhkmSPvjgg7ANBAAAECkh/dHV/oBPjQEA0P9E/VNjf//737t9o+PGjevVMAAAAJHU7RDKzMyUw+HQd72AxDlCAACgv+h2CB05ciSccwAAAERct0PoqquuCuccAAAAEdftEHr77be7faO33357r4YBAACIpG6H0MyZM7u1jnOEAABAf9HtEAoEAuGcAwAAIOLierJ42rRpam5uDl5fu3atTp8+Hbz+9ddf6/rrrw/ZcAAAAOHUoxCqqqpSa2tr8PqaNWt06tSp4PULFy7o4MGDoZsOAAAgjHoUQv/Lsi+lBgAAMeZ7hRAAAEB/1qMQcjgcnX51vqtfoQcAAOgPuv2pMenfb4XdfffdcjqdkqRz585p/vz5uuyyyySpw/lDAAAAfV2PQqioqKjD9V/96led1hQWFn6/iQAAACKkRyH08ssvh2sOAACAiONkaQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADW6hMhVF5eroyMDCUmJionJ0d79uzp1n4VFRVyOByaOXNmeAcEAAAxKeohtHXrVnk8HpWUlKiurk7jx49Xfn6+Tpw4ccn9jh49ql//+teaMmVKhCYFAACxJuohtGHDBt17772aO3eurr/+em3atEmDBw/WSy+9dNF92tvbddddd2nVqlUaNWrUJW+/tbVVfr+/wwUAAECKcgi1tbWptrZWeXl5wW1xcXHKy8tTTU3NRfd7/PHHlZaWpnvuuec776O0tFTJycnBi9vtDsnsAACg/4tqCDU1Nam9vV0ul6vDdpfLJa/X2+U+H330kV588UVt3ry5W/dRXFys5ubm4OX48ePfe24AABAbevSjq9F25swZzZkzR5s3b1Zqamq39nE6nXI6nWGeDAAA9EdRDaHU1FTFx8fL5/N12O7z+ZSent5p/WeffaajR49qxowZwW2BQECSNGDAAB08eFCjR48O79AAACBmRPWtsYSEBGVlZam6ujq4LRAIqLq6Wrm5uZ3WjxkzRvv371d9fX3wcvvtt+vWW29VfX095/8AAIAeifpbYx6PR0VFRcrOztbEiRNV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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 6))\n",
        "\n",
        "runner_up_count.plot(kind=\"bar\")\n",
        "\n",
        "plt.title(\"ICC Men's Cricket World Cup Runner-Ups\")\n",
        "plt.xlabel(\"Team\")\n",
        "plt.ylabel(\"Number of Runner-Up Finishes\")\n",
        "\n",
        "plt.xticks(rotation=45)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 625
        },
        "id": "A1So95YxlsM_",
        "outputId": "84eea8a0-a22d-4c88-df8a-06f8e5f7daae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA04AAAJgCAYAAAC9cTNzAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAAfc1JREFUeJzt3XmcjeX/x/H3mRnGNiP7vgxjyb4kjLUoZE2WL8ouFRFSKEp9hYSSJRJSiQoViWRJjLJk3/d97Axjn/n8/vCb83UynDk1M2fMvJ6Pxzw4133f53zOueecOe/7uu7rdpiZCQAAAABwTz7eLgAAAAAAEjuCEwAAAAC4QXACAAAAADcITgAAAADgBsEJAAAAANwgOAEAAACAGwQnAAAAAHCD4AQAAAAAbhCcAAAAAMANghMAJHMHDx6Uw+HQtGnTPNru7bfflsPh0JkzZ+KnsESuZs2aqlmzptv1li9fLofDoeXLl8d7TQCA+ENwAhCvpk2bJofDoXXr1t21bOPGjXr22WeVJ08e+fv7K2PGjKpdu7amTp2qyMhIl3WvXbum0aNHq2LFikqfPr1SpUqlwoULq3v37tq9e/d9a4j+4upwOPTll1/GuE6VKlXkcDhUokSJf/5kYyE6pMTll2hPXsfE6sqVK3r77bdj9bqsWbNGDodDo0ePvmtZ48aN5XA4NHXq1LuWVa9eXbly5YqLcuPVvn371LVrVxUoUECpUqVSYGCgqlSpoo8++khXr15N8Hrat2/vfP84HA75+/urcOHCGjRokK5du5bg9SS0+32GSVKDBg2UP3/+hC0KgFf4ebsAAMnT5MmT9cILLyhbtmx67rnnVKhQIV26dElLlixRp06ddOLECQ0YMECSdObMGdWtW1fr169XgwYN1Lp1a6VLl067du3SzJkzNWnSJN24ccPtY6ZKlUozZszQs88+69J+8OBBhYaGKlWqVPHyXOOTJ6/jveTLl09Xr15VihQpEqjqu125ckWDBw+WJLe9OOXKlVOaNGm0cuVK9erVy2VZaGio/Pz8tGrVKnXo0MHZfuPGDa1du1YNGzaM89rj0k8//aTmzZvL399fbdu2VYkSJXTjxg2tXLlSffv21bZt2zRp0qQEr8vf31+TJ0+WJF28eFE//PCD3n33Xe3bt09fffVVgtcDAN5AcAKQ4P744w+98MILqly5shYsWKCAgADnsldeeUXr1q3T1q1bnW3t27fXhg0b9N133+mZZ55xua93331Xb7zxRqwe96mnntKPP/6oM2fOKHPmzM72GTNmKFu2bCpUqJDOnz//L59dwvH0dfy7W7duKSoqSilTpnygQqOfn58qVqyoVatWubTv2rVLZ86cUevWrbVy5UqXZevXr9e1a9dUtWrVf/34V65cUZo0af71/fzdgQMH9J///Ef58uXT0qVLlSNHDueybt26ae/evfrpp5/i/HFjw8/Pz+WAw0svvaSQkBB9/fXXGjVqlLJly+aVuuLKne8FALgXhuoBSHCDBw+Ww+HQV1995fJlP9ojjzyi9u3bS5L+/PNP/fTTT+rUqdNdoUm6fST8gw8+iNXjNm7cWP7+/vr2229d2mfMmKEWLVrI19c3xu2+/PJLlS9fXqlTp1bGjBn1n//8R0eOHHFZp2bNmipRooS2b9+uxx57TGnSpFGuXLn0/vvvu60rLCxMHTp0UO7cueXv768cOXKocePGOnjw4H238+R1jB4i+MEHH+jDDz9UwYIF5e/vr+3bt9/zHKedO3eqRYsWypIli1KnTq0iRYq4DamHDh1ScHCwSpQooZMnT0qSLly4oFdeecU5lDA4OFjDhw9XVFSUs7YsWbK4PCeHw6G33377no9TtWpVnTx5Unv37nW2rVq1SoGBgXr++eedIerOZdHbRRs/fryKFy8uf39/5cyZU926ddOFCxdcHid6v65fv17Vq1dXmjRp7tuDd/ToUTVp0kRp06ZV1qxZ1atXL12/fv2+r1m0999/X5cvX9Znn33mEpqiBQcHq2fPnpLuf17a31+76HPRovdnYGCgMmXKpJ49e/7joXYOh0NVq1aVmWn//v33fOxo+fPnd/4uSv8b/rZq1Sr17t1bWbJkUdq0afX000/r9OnTd23boEEDrVy5Uo8++qhSpUqlAgUKaPr06Xc9jrvfNen+74W4cOf9jx49Wvny5VPq1KlVo0aNuw5k/NP3PgDvoMcJQIK6cuWKlixZourVqytv3rxu1//xxx8lSc8999y/fuw0adKocePG+vrrr/Xiiy9KkjZt2qRt27Zp8uTJ2rx5813bDBkyRAMHDlSLFi3UuXNnnT59Wh9//LGqV6+uDRs26KGHHnKue/78edWtW1dNmzZVixYt9N133+n1119XyZIlVa9evXvW9cwzz2jb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ly5V2bJlY9zG09cx2r/9ohuTZ555Rp9//rm++uorde3a1WVZVFSUnnjiCb322msxblu4cOF//LjRwWnVqlUKDQ1VyZIlnfskJCRE169f19q1a7Vy5Ur5+fk5Q5Wn4uM1+7vAwEDlzJnzvrMg3ulevTyeXLfLk54iX19f1a5d23m7Tp06Klq0qLp27eo8D/F+7lVXbN8zsVnP09+1v+/Xv0/IMXXqVLVv39454+S9rqF15cqVfzwr5T957wPwHoITgASVJk0aPf7441q6dKmOHDmiPHny3Hf9hg0baujQofryyy/jLDhVrVpVefPm1fLlyzV8+PB7rlewYEGZmYKCgv7VF/zYKFiwoPr06aM+ffpoz549KlOmjEaOHHnPC/Z6+jp6okCBApIU6y/xI0aMkJ+fn1566SUFBAS49OAVLFhQly9fdvnSHZN/MtzrzgkiVq9erSpVqjiX5cyZU/ny5dOqVau0atUqlS1b1jmFeL58+STdnr48+rlKt6/1dODAAbe13ku+fPm0detWmZnL89m1a1estm/QoIEmTZqk1atXq3LlyvddN7pn5u+zAP69t+xOe/bscell2bt3r6Kiov7RJAQ5cuRQr169NHjwYP3xxx/OUJohQ4a7arpx44ZOnDjh8WN4Kra/a/eyePFil9vRk07c+fsS02fQ7t27Y+yd3bNnT4zr/v319vS9D8B7OMcJQIJ76623ZGZ67rnndPny5buWr1+/Xp9//rkkqXLlyqpbt64mT56s77///q51b9y4oVdffdWjx3c4HBozZozeeuut+87W17RpU/n6+mrw4MF3HQE3M509e9ajx43JlStX7poSumDBggoICHA7jbUnr6MnsmTJourVq2vKlCk6fPiwy7KYes8cDocmTZqkZs2aqV27di49EC1atNDq1au1aNGiu7a7cOGCbt26JUnOUPP3L933kzNnTgUFBWnJkiVat27dXbPRhYSE6Pvvv9euXbtcpiGvXbu2UqZMqTFjxrg8n88++0wXL15U/fr1Y13DnZ566ikdP35c3333nbPtypUrsb5g7Wuvvaa0adOqc+fOzqnc77Rv3z599NFHkm73UGXOnPmu83bGjx9/z/sfN26cy+2PP/5Yku474+P9vPzyy0qTJo2GDRvmbCtYsOBdNU2aNMmjnrB/Kra/a/dSu3Ztl5/oHqjy5csra9asmjx58l3vye+//17Hjh2L8TWMXhZtzZo1+vPPP53r/pv3PgDvoMcJQIILCQnRuHHj9NJLL6lo0aJ67rnnVKhQIV26dEnLly/Xjz/+qP/+97/O9adPn64nn3xSTZs2VcOGDVWrVi2lTZtWe/bs0cyZM3XixIlYX8spWuPGjdW4ceP7rlOwYEH997//Vf/+/XXw4EE1adJEAQEBOnDggObOnavnn3/e49D2d7t371atWrXUokULFStWTH5+fpo7d65Onjyp//znP/fd1tPX0RNjxoxR1apVVa5cOT3//PMKCgrSwYMH9dNPP2njxo13re/j46Mvv/xSTZo0UYsWLbRgwQI9/vjj6tu3r3788Uc1aNDAOX10RESEtmzZou+++04HDx5U5syZlTp1ahUrVkyzZs1S4cKFlTFjRpUoUcLteVZVq1bVF198IUkuPU7Rr8/XX3/tXC9alixZ1L9/fw0ePFh169ZVo0aNtGvXLo0fP14VKlRwmeDDE126dNHYsWPVtm1brV+/Xjly5NAXX3wR64vlFixYUDNmzFDLli318MMPq23btipRooRu3Lih0NBQffvtty7XQurcubOGDRumzp0765FHHtGKFSu0e/fue97/gQMH1KhRI9WtW1erV6/Wl19+qdatWzunaPdUpkyZ1KFDB40fP147duzQww8/rM6dO+uFF17QM888oyeeeEKbNm3SokWLXC44HV9i+7vmqZQpU+qDDz5Qu3btVKFCBbVs2VKZMmXShg0bNGXKFJUqVSrGCUCCg4NVtWpVvfjii7p+/bo+/PBDZcqUyTmU8N+89wF4iVfm8gOQbNxvKt/169db69atLWfOnJYiRQrLkCGD1apVyz7//HOXaaLNzK5cuWIffPCBVahQwdKlS2cpU6a0QoUK2csvv2x79+69bw13Tkd+P3+fjjza7NmzrWrVqpY2bVpLmzatFS1a1Lp162a7du1yu227du1cpir+uzNnzli3bt2saNGiljZtWkufPr1VrFjRZUprd2LzOkZPkRzT1Mf3mtp669at9vTTT9tDDz1kqVKlsiJFitjAgQOdy++cjjzalStXrEaNGpYuXTr7448/zMzs0qVL1r9/fwsODraUKVNa5syZLSQkxD744AO7ceOGc9vQ0FArX768pUyZMtZTk0+cONEkWa5cue5a9tdff5kkk2QnT568a/nYsWOtaNGi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tGl66623NH/+fDkcDv3888/y87t7U4fDQXACAAAAkOTEKjgVKVJEM2fOlCT5+PhoyZIlypo1a7wWBgAAAACJRayC052ioqLiow4AAAAASLQ8Dk6StG/fPn344YfasWOHJKlYsWLq2bOnChYsGKfFAQAAAEBi4PF1nBYtWqRixYppzZo1KlWqlEqVKqU///xTxYsX1+LFi+OjRgAAAADwKo97nPr166devXpp2LBhd7W//vrreuKJJ+KsOAAAAABIDDzucdqxY4c6dep0V3vHjh21ffv2OCkKAAAAABITj4NTlixZtHHjxrvaN27cyEx7AAAAAJIkj4fqdenSRc8//7z279+vkJAQSdKqVas0fPhw9e7dO84LBAAAAABv8zg4DRw4UAEBARo5cqT69+8vScqZM6fefvtt9ejRI84LBAAAAABv8zg4ORwO9erVS7169dKlS5ckSQEBAXFeGAAAAAAkFv/oOk7RCEwAAAAAkgOPJ4cAAAAAgOSG4AQAAAAAbhCcAAAAAMANj4LTzZs3VatWLe3Zsye+6gEAAACARMej4JQiRQpt3rw5vmoBAAAAgETJ46F6zz77rD777LP4qAUAAAAAEiWPpyO/deuWpkyZol9//VXly5dX2rRpXZaPGjUqzooDAAAAgMTA4+C0detWlStXTpK0e/dul2UOhyNuqgIAAACARMTj4LRs2bL4qAMAAAAAEq1/PB353r17tWjRIl29elWSZGZxVhQAAAAAJCYeB6ezZ8+qVq1aKly4sJ566imdOHFCktSpUyf16dMnzgsEAAAAAG/zODj16tVLKVKk0OHDh5UmTRpne8uWLbVw4cI4LQ4AAAAAEgOPz3H65ZdftGjRIuXOndulvVChQjp06FCcFQYAAAAAiYXHPU4REREuPU3Rzp07J39//zgpCgAAAAASE4+DU7Vq1TR9+nTnbYfDoaioKL3//vt67LHH4rQ4AAAAAEgMPB6q9/7776tWrVpat26dbty4oddee03btm3TuXPntGrVqvioEQAAAAC8yuMepxIlSmj37t2qWrWqGjdurIiICDVt2lQbNmxQwYIF46NGAAAAAPAqj3ucJCl9+vR644034roWAAAAAEiU/lFwOn/+vD777DPt2LFDklSsWDF16NBBGTNmjNPiAAAAACAx8Hio3ooVK5Q/f36NGTNG58+f1/nz5zVmzBgF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saJ99NFHLuv95z//sY4dOzqPvvXu3dtWr15tp0+fTtB6k5uDBw/a1q1bzczs2rVrzvZTp06ZmVmXLl2sVatWzl6/Fi1aWPbs2S0kJMTCw8PpaUgiovfj/PnzrWXLllarVi2bPXu2mZkdO3bMWrRoYRUrVrRXXnnFfv75Z+vevbvlzp3bjhw54s2yk6xx48ZZgwYNbP369c62HTt2WIECBezy5cvOtjNnzljGjBmtR48edvr0aXv99detRIkSzvcvEqe5c+damjRp7M0337S3337bateubUFBQbZv3z7nOqtWrbJXXnnFHnroIdu4caMXq03epk+fbj4+PvbOO+84v59Ef17OmTPHsmTJYmFhYd4s0WMEp2Qi+hfWzFy6TCMjI+3555+3SpUq2U8//eRsP336tHXp0sVCQ0Pt1q1bCVorbtu2bZsVL17cnnjiCTt79qyzrWXLllatWjWbOHGic91evXpZhgwZ7N1337V27dpZQECA7dmzx1ulJ3l//fWXhYeHO28vW7bMQkJCXL4IX7t2zSpWrGhvvvmmmf3vvTZmzBgCbRK0dOlSS5MmjXXo0MEaNWpkvr6+9sYbb9i1a9fs+PHj9s4771jRokWtYMGCVrx4cfvrr7+8XXKStXjxYsudO7c999xztm7dOjO7PZSrePHiznVu3rxpZmZTp061VKlSWb58+Sx79uzsl0QuLCzMKleubB9//LGZ3R4KnSlTJuvVq5dznZMnT1rnzp2tVq1atnnzZm+VmqxEh6Hr16/b9evXXZaNHz/efHx8bNiwYc71ov+980DGg4LglAzceVR76NCh1qBBA6tVq5YtWrTIbty4YZs3b7bmzZtbkSJF7N1337WvvvrKateubSEhIc5to//IIOFERkbaV199ZdWrV7d69eo5j4Ju377d2rdvb5UrV7bx48c71+/QoYOVL1/eqlWrxhG2eBIVFWXLly83h8Phcv7Y/v37LWvWrFajRg07duyYmd1+z3To0MGqV69uX3zxhb366quWJ08eehmSoJMnT9qwYcNszJgxzraJEydaQECA9e/f3yVkHz169K7z4hB3ov9m/fbbbxYUFGStW7e2bdu22cqVKy04ONiuXr161zb79++3ZcuW2dGjRxO6XNzHhx9+aNOnT3dpO378uBUpUsQOHDhgBw8etNy5czvP7TUz+/nnn+3SpUt2/Phxl3OCEX+i33MLFy60Jk2aWPXq1a1jx44WFhbmXDZu3Djz8fGx999//4EfaUFwSuLu7GkaPXq0pU+f3t5++22rXLmyFShQwD744AO7fv267d692wYPHmxZs2a18uXLW61atezGjRtmFvMQP8Sv6Nc8MjLSvv76a6tSpYrVrVvXbXg6e/asXblyxSs1Jyevv/66pUqVyiZMmOD8Unzw4EErWLCgValSxRmeFi1aZI0aNbLcuXNbiRIlXIYO4cEXFRVlu3fvNofDYblz53bpBTYz++STTyxdunQ2cOBAO3TokJeqTH6i/+4tX77cgoKCrEuXLjZq1CgrXry4zZkzx7755htbuHChLV682KZOnUqvRCITGRlpx48fty5dutju3btdlu3fv985QiYoKMg6d+7s3N+7du2yDh062PLly71RdrL2/fffW2BgoHXv3t2mT59uuXLlsvr169vatWud32cmTJhgDofDPvzwQy9X++8QnJKJbdu22fPPP2+LFy92tvXq1csefvhhe//9951f/i5cuGAXLlygpykRiB4iGRkZaTNmzLhneKpWrZqNHDnSm6UmG9EHE8zM3njjDfP397fJkyc7ZwY6cOCAFSxY0CpXruw8N+3cuXN25MgRhuclYe+++645HA7r2bOnS++Smdmnn35qDofD/vvf/zLs2Qt+/fVXCwoKsty5c1tgYKCVL1/e8uXLZyVKlLCiRYtazpw5be/evd4uE3eIPl80ehhXaGioTZ482bm8RYsWMc58+Prrr1uZMmXoOUxgO3bssGLFitnYsWPNzCw8PNxy5cplqVKlsrJly9q6deuc4Xby5Mm2fft2b5b7rxGckoHvvvvOsmbNavnz57fff//dZVmvXr2sePHi9v7779uJEydclt3ZWwXvunXrln355ZcxhqdmzZrZk08+aefPn/dukcnAncOAfvzxRwsMDLRMmTLZxIkTnecORoenatWq8Qc8GXnnnXfM4XDY2LFjXc4jNbt9Hs3OnTu9VFnyEP3e3Lx5s82fP982bNjg/OIdPWzvmWeesdDQUOc5GDdv3nwgz7FIyqZNm2bVqlVzHoy6cOGCtWnTxkqVKuUMT5cvX7Y6depYrly57IsvvrBPP/3UunfvbgEBAQxTj0d3jj668yDQ5s2b7Z133rGbN2/asWPHrECBAvbyyy/byZMnLUeOHFavXj0LDQ1NMqOXCE7JRLt27SxlypT23nvv3fWH4tVXX7UsWbLYl19+6aXqEC36g2X9+vU2adIkmz59uq1Zs8bM7g5P0T0YO3futOPHj3ut5uRm3rx55uvra8OHD7fBgwdby5YtLUWKFDZhwgTnF+aDBw9ahgwZrG7duvQyJCHR789t27bZihUrbMmSJS4HmAYOHGg+Pj42duxYvpB7wbfffmtZsmSx7NmzW9GiRa1bt27O81yie57atm1rf/zxh5crRUyioqLs008/tQoVKtjTTz/tDE8bNmywDh06WEhIiH322WdmdntSiFatWlmJEiWsRIkS1rhxY9u0aZM3y08W7hw5sWjRIvv2228tMjLS2Yv03HPPWevWrZ3n/9apU8ccDofVqFHDZebZBxnBKYm5Xy9Rq1atrGjRojZ9+vS7Loo6ZswYvuB5WfSXstmzZ1v27NmtYsWKVqVKFStatKjNnTvXzP4XnmrUqGGVK1fm5NcEdu3aNatdu7a99NJLLu19+/a1FClS2MSJE51/7A8dOsTMhknInVPo5syZ00qVKmUpUqSwZ5991latWuVcb+DAgZYqVSobMWIEF59OQMeOHbM6derYZ599ZocPH7b33nvPqlSpYv/5z3+cn5NLly61wMBA69KlS5L5EpfU3Lhxw2bMmGE1a9a0p556yvl5unnzZnvuueescuXKNmXKFOf6R48etcuXL/NeSwAXLlywbNmy2cCBA+3HH380h8Nh33//vXP5zZs3rUaNGjZixAhnW69evWzNmjUuU8U/6AhOScidoen333+32bNn219//eWcytrMrHnz5vbwww/HGJ7MjPDkZb/99ptlyZLFJkyYYGa3p7lOnTq1pU2b1tkjeOvWLfvss8+sbt26nHCegKKiouzmzZtWpUoVe+utt8zM9ZynJk2aWM6cOe3jjz++a6gWHlx3fiYuXrzYMmbMaJMmTXLedjgc9vTTT9uKFSuc6/Xu3dsyZcpk586dS/B6k6N169ZZ+/btrUWLFs7XPCoqyiZMmGAhISEu4em3337jgEYiFX1O9ZYtW2zw4MGWIUMGa968uUt4atu2rVWuXNk+/fRTb5aaLN24ccO+/fZb8/f3N39/f5s5c6aZ/e+7540bN6x06dJWr149W7BggfXp0+eBvE6TOwSnJOLOsaP9+vWzXLlyWdGiRS179uzWo0cP57UszG6fWFmyZEmbMGECR90SkaioKOvfv7+9+uqrZmZ25MgRy5cvn7Vp08Y6depkadKkcR7duXXrFlMae0mHDh2saNGizmmNo8NTnz59LH369JY1a1bON0sCZsyY4ZwdMTIy0i5fvmwvv/yyvfHGG2Zmtm/fPgsODrYmTZpY7ty57bHHHnMJT1xENWFERkbagAEDLG/evFawYEGXA4i3bt2yCRMmWPXq1e2pp55yOYiIxGnmzJn28MMPW5s2baxkyZKWMWNGa9iwoTMQb9682Tp06GDFihWzL774wsvVJj+bNm0yh8NhDofDBg8e7GyPDr07duywXLlyWcGCBa1gwYJJ8rpoBKck4M6Z74YPH265cuWy3377zcxun78UEBBgzz77rPNcGTOzWrVqWZs2bZLMyXoPqujXf9myZbZ582Y7fPiwrVixwi5fvmwVK1a0zp07m9ntaXX9/PzM4XDY119/7c2Sk43ofXPs2DE7fPiwMyht3brVypUrZw0bNnQ58NCnTx9bsmQJs+clATt27LBSpUrZY4895pw05+rVq/bLL7/Ynj177Pz581auXDnr1KmTmd2+doy/v7/VqVPHOQEPn60JJyIiwoYMGWK5c+e2bt26uVyS4datWzZq1CirU6cOk7Ukcnv37rWcOXPa2LFjnRN4jBkzxh599FFr1KiRyzlPL7zwgh04cMCL1SYf0Z9lZ8+etcuXL9umTZts5syZliJFChswYIBzvejvotevX7fDhw8n2b+FBKcH2KhRo5z/v3Xrlh07dsyaNm3qPArzww8/WPr06a19+/aWJ08ea9mypa1du9a5TfSROf7Ae9fSpUstICDAvvnmG2dbaGioPfLII85rWGzdutWaNGlib7/9NrNzJaDvvvvOihcvbpkzZ7Y2bdrYzz//bGZmc+fOtbJly1rBggWtR48e1rRpU0uVKhX7JgmZNWuWPf7441a7dm3n5CvRQzBnzZplFSpUcA6VnTt3rlWqVMkeffRRLnAcz6L/XkWHo+gv2BERETZw4ECrVKmS9enTx+WgRmRkJL3AD4A//vjDsmTJ4nJdrStXrtioUaMsMDDQWrVq5ex5it7viF/R77cff/zRnn76aVu4cKHdvHnTrl+/blOmTDE/Pz978803netPnDjRvv32W2+VmyAITg+olStXmp+fn7Vu3drZdvnyZVuyZImdPXvW1q5da7lz53Ze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u3ZNqVKl8nYZQLIQHh6uwMBAXblyRf369dO1a9fUoUMH9ezZU7Vr19b8+fN15MgRhYaGcl2SRGbXrl164YUXlCFDBg0ZMoT9k0hEn9N0/vx5ZciQwdl+8eJFVa9eXdmyZdMvv/yisLAwNWzY0Dmd/9WrV7Vq1SpNmTJFK1euZHgekhV6nIB/iNAEJIzNmzercuXK+uabb5QmTRoNGjRIP/74o/MSALly5VKBAgV08eJFDR48mB6nRKZIkSKaNWuWpk6dSmhKRHx8fLRv3z4VLlxYTZo00alTp3TlyhWlT59en376qX7//XeNGDFC2bNn1zfffKOsWbOqT58+GjRokHbu3Knff/+d0IRkhxNpAACJUvQR8Vu3bql27dp67rnn9Ouvv6pr166aPXu23nvvPZUqVUrdunVTq1at9MYbb6hHjx7OoURIPLJmzertEhCDqKgo3bp1Sz/++KOuXr2qp556SrVq1dKjjz6qF198UbNmzVKNGjX06KOP6tdff9WhQ4eULl06+fv7K126dN4uH0hwDNUDACQq0TOtRUREKG3atIqMjJSvr68WLVqk0aNH69KlS8qWLZuyZcum4OBg9enTx9slAw+MOw9I+Pn5acyYMTp48KDSpEmjs2fPav369XrnnXeUKVMmPffcc2rdurUGDhzIRB6AGKoHAEhEokPTwoUL9dxzz+nxxx9XgwYNtHPnTtWpU0cTJ07UCy+8oN27d2vixInq27evdu3a5e2ygUQv+jj5lStXJP1v9t7SpUtrx44dqlKlikaNGqW2bduqVatWWrlypYKCgjR69Ght27bNa3UDiQnBCQCQaDgcDv34449q2rSpypQpo65du+r69euqUKGC9u3bp3z58um5557Tn3/+qQ4dOih37twMzQNiweFwKCwsTMWKFdMbb7yhw4cPS5Jq1KihKlWqqG3btjp37py6d++uefPmaevWrfL19dXFixc1YMAARUZG3jULH5DcMFQPAOA1f78A6uXLl9WkSRM98cQTev3113X06FFVr15dTzzxhCZOnHjX9n+fEQzAvV24cEFjxozRqFGjVL58eTVs2FCvvPKKJKl9+/aSpI8++kjp06fXyZMntX37do0cOVJDhw5VyZIlvVc4kEgQnAAACe7v5zFFn3dx5swZPfroo1q0aJEyZMigMmXKqH79+s7Q9MUXX6hJkyYKCAjw8jMAHlzbt2/XW2+9pY0bNyp37tz65JNPtHnzZv3000969tlnVbt2bee6fz+4ASRnDNUDACQ4h8OhU6dOKX/+/Prmm2/k4+MjM1PmzJlVsmRJff31184j4mPHjpUknT59WnPnztWCBQu8XD3wYCtWrJgmTpyoDz/8UBcvXtRTTz2lv/76S1u3btW3337rsi6hCfgfghMAwCt8fHzUqFEjPffcc/rhhx/kcDh08+ZNFSxYUCNHjlSxYsU0YcIEpUiRQpI0atQo7d69WyEhIV6uHHjwZcyYUfXr19dff/2lRo0aaePGjQoLC9Onn36qyZMne7s8IFFiqB4AIEHENOTn1KlTGjJkiD7++GPNnj1bTz/9tM6fP69WrVrp9OnTqlq1qgoXLqz169drzpw5Wr58ucqUKeOdJwAkMXe+J5cvX66FCxdq/PjxWrNmjYoWLerl6oDEh+AEAIh30ecwRUREKDIyUoGBgc5lJ06c0Hvvvadx48bp22+/1TPPPKOzZ89q2LBhWrt2rSIiIlS4cGH1799fJUqU8OKzAJKevx/QCA8Pd3l/AvgfghMAIEHs2bNHLVq0ULp06dSlSxdlz55dTz75pCTp+vXr6tOnj8aPH69Zs2apefPmunXrlnx8fHTz5k35+vo6rzsDAIA38FcIABDvoqKiNG3aNG3atEmpUqXShQsXdOXKFWXMmFGPPvqoOnbsqA4dOihTpkxq2bKlAgMDVadOHZmZ/P39vV0+AAD0OAEAEkZYWJiGDx+uffv2KTg4WN26ddNXX32l33//XZs3b1bGjBlVoEABrV+/XqdOndLy5ctVvXp1b5cNAIAkepwAAAkke/bs6tu3r9577z2tXLlShQoV0qBBgyRJf/75p44fP65JkyYpa9asOnXqlDJnzuzligEA+B96nAAACSp6Mog///xTTZo00YABA5zLbt68qaioKF28eFFZs2b1YpUAALgiOAEAElxYWJiGDBmitWvXqkmTJurXr58k6datW0wCAQBIlAhOAACviA5PGzZsUK1atTR48GBvlwQAwD35eLsAAEDylD17dr3xxhsqVKiQQkNDdfbsWW+XBADAPdHjBADwqpMnT0qSsmXL5uVKAAC4N4ITAAAAALjBUD0AAAAAcIPgBAAAAABuEJwAAAAAwA2CEwAAAAC4QXACAAAAADcITgAAAADgBsEJAAAAANwgOAEAAACAGwQnAMADxeFw3Pfn7bff9naJAIAkyM/bBQAA4IkTJ044/z9r1iwNGjRIu3btcralS5fOG2UBAJI4epwAAA+U7NmzO3/Sp08vh8Ph0jZz5kw9/PDDSpUqlYoWLarx48e7bP/666+rcOHCSpMmjQoUKKCBAwfq5s2bzuVvv/22ypQpoylTpihv3rxKly6dXnrpJUVGRur9999X9uzZlTVrVg0ZMiShnzoAwIvocQIAJBlfffWVBg0apLFjx6ps2bLasGGDunTporRp06pdu3aSpICAAE2bNk05c+bUli1b1KVLFwUEBOi1115z3s++ffv0888/a+HChdq3b5+aNWum/fv3q3Dhwvrtt98UGhqqjh07qnbt2qpYsaK3ni4AIAE5zMy8XQQAAP/EtGnT9Morr+jChQuSpODgYL377rtq1aqVc53//ve/WrBggUJDQ2O8jw8++EAzZ87UunXrJN3ucRoxYoTCwsIUEBAgSapbt6527dqlffv2ycfn9mCNokWLqn379urXr188PkMAQGJBjxMAIEmIiIjQvn371KlTJ3Xp0sXZfuvWLaVPn955e9asWRozZoz27duny5cv69atWwoMDHS5r/z58ztDkyRly5ZNvr6+ztAU3Xbq1Kl4fEYAgMSE4AQASBIuX74sSfr000/vGj7n6+srSVq9erXatGmjwYMHq06dOkqfPr1mzpypkSNHuqyfIkUKl9sOhyPGtqioqLh+GgCARIrgBABIErJly6acOXNq//79atOmTYzrhIaGKl++fHrjjTecbYcOHUqoEgEADzCCEwAgyRg8eLB69Oih9OnTq27durp+/brWrVun8+fPq3fv3ipUqJAOHz6smTNnqkKFCvrpp580d+5cb5cNAHgAMB05ACDJ6Ny5syZPnqypU6eqZMmSqlGjhqZNm6agoCBJUqNGjdSrVy91795dZcqUUWhoqAYOHOjlqgEADwJm1QMAAAAAN+hxAgAAAAA3CE4AAAAA4AbBCQAAAADcIDgBAAAAgBsEJwAAAABwg+AEAAAAAG4QnAAAAADADYITAAAAALhBcAIAAAAANwhOAAAAAOAGwQkAAAAA3CA4AQAAAIAb/wfoDdhwb0SiQgAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "most_runner_up = runner_up_count.idxmax()\n",
        "runner_up_times = runner_up_count.max()\n",
        "\n",
        "print(\"Team with the most Runner-Up finishes:\", most_runner_up)\n",
        "print(\"Number of Runner-Up finishes:\", runner_up_times)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sMkv26h-m2Jg",
        "outputId": "0c2db7b0-5d79-49ed-b9f7-1d2390fdbc46"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Team with the most Runner-Up finishes: England\n",
            "Number of Runner-Up finishes: 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "host_count = world_cup_df[\"Host\"].value_counts()\n",
        "\n",
        "print(host_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lPUZKESUmePA",
        "outputId": "6f3e2ce7-fc41-440b-898a-e5831c3ea084"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Host\n",
            "England                          4\n",
            "Australia & New Zealand          2\n",
            "India & Pakistan                 1\n",
            "India, Pakistan & Sri Lanka      1\n",
            "South Africa                     1\n",
            "West Indies                      1\n",
            "India, Sri Lanka & Bangladesh    1\n",
            "England & Wales                  1\n",
            "India                            1\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(12, 6))\n",
        "\n",
        "host_count.plot(kind=\"bar\")\n",
        "\n",
        "plt.title(\"ICC Men's Cricket World Cup Hosts\")\n",
        "plt.xlabel(\"Host\")\n",
        "plt.ylabel(\"Number of Tournaments\")\n",
        "\n",
        "plt.xticks(rotation=60)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 738
        },
        "id": "1i-AecNMmdIn",
        "outputId": "6cb0981b-7a3e-4050-bc6d-90c069afdae0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA+kAAALRCAYAAAAnY+ILAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAA1p9JREFUeJzs3Xd8Tffjx/H3TWQYSUqNiL1qxaYENWpvpXatWkVra0Vr01ClaLWlLVGjNlWUqlmrds3as4QgxExIPr8//HK/UqNum+Qe8no+HvfR3jPufeece6/7vmfZjDFGAAAAAADA6VycHQAAAAAAADxASQcAAAAAwCIo6QAAAAAAWAQlHQAAAAAAi6CkAwAAAABgEZR0AAAAAAAsgpIOAAAAAIBFUNIBAAAAALAISjoAAAAAABZBSQcAwKJOnTolm82m4OBgh+YbPHiwbDabLl++HD/BLK5ChQqqUKHCP063bt062Ww2rVu3Lt4zAQDwrCjpAJBIBQcHy2azaceOHY+M27Nnj9566y1lypRJHh4eSpUqlSpXrqypU6cqKioq1rR3797VZ599ppIlS8rHx0eenp565ZVX9O677+rIkSNPzRBTkmw2m2bMmPHYacqUKSObzSZ/f/9//8c+g5hCHJeFzZHlaFW3b9/W4MGDn2m5bNu2TTabTZ999tkj4+rVqyebzaapU6c+Mq5cuXLKkCFDXMSNV8ePH1enTp2UPXt2eXp6ytvbW2XKlNH48eN1586dBM/Tpk0bpUiR4onjbTab3n333Xh57oMHD2rw4ME6depUvDw+ACRmSZwdAABgLd9++63eeecdpUuXTi1btlSuXLl048YNrV69Wu3atdOFCxfUv39/SdLly5dVvXp17dy5U7Vr11bz5s2VIkUKHT58WLNnz9bkyZMVGRn5j8/p6empWbNm6a233oo1/NSpU9q8ebM8PT3j5W+NT44sxyfJkiWL7ty5Izc3twRK/ajbt29ryJAhkvSPW6eLFi2qZMmSaePGjerZs2escZs3b1aSJEm0adMmtW3b1j48MjJS27dvV506deI8e1xatmyZGjVqJA8PD7Vq1Ur+/v6KjIzUxo0b1bdvXx04cECTJ092dswEc/DgQQ0ZMkQVKlRQ1qxZnR0HAF4olHQAgN3WrVv1zjvvKCAgQMuXL5eXl5d9XI8ePbRjxw7t37/fPqxNmzbavXu35s+fr4YNG8Z6rGHDhunDDz98puetWbOmlixZosuXLyt16tT24bNmzVK6dOmUK1cuhYWF/ce/LuE4uhz/7v79+4qOjpa7u/tz9QNFkiRJVLJkSW3atCnW8MOHD+vy5ctq3ry5Nm7cGGvczp07dffuXZUtW/Y/P//t27eVLFmy//w4f3fy5Ek1bdpUWbJk0Zo1a5Q+fXr7uK5du+rYsWNatmxZnD8vACBxYnd3AIDdkCFDZLPZNHPmzFjFMkbx4sXVpk0bSdLvv/+uZcuWqV27do8UdEny8PDQp59++kzPW69ePXl4eGjevHmxhs+aNUuNGzeWq6vrY+ebMWOGihUrpqRJkypVqlRq2rSpzp49G2uaChUqyN/fXwcPHlTFihWVLFkyZciQQZ988sk/5goJCVHbtm2VMWNGeXh4KH369KpXr94/7uLryHKM2c3+008/1bhx45QjRw55eHjo4MGDTzwm/c8//1Tjxo2VJk0aJU2aVLlz5/7HH0ROnz6tnDlzyt/fXxcvXpQkXbt2TT169LDvjp8zZ06NGjVK0dHR9mxp0qSJ9TfZbDYNHjz4ic9TtmxZXbx4UceOHbMP27Rpk7y9vdWxY0d7YX94XMx8Mb788kvlz59fHh4e8vPzU9euXXXt2rVYzxOzXnfu3Kly5copWbJkT90z4dy5c6pfv76SJ0+utGnTqmfPnoqIiHjqMovxySef6ObNm/ruu+9iFfQYOXPmVPfu3SU9/TwCf192MecOiFmf3t7eevnll9W9e3fdvXv3mbI56tKlS2rXrp3SpUsnT09PFSpUSNOmTXtkutmzZ6tYsWLy8vKSt7e3ChQooPHjx0t6cKhMo0aNJEkVK1a0vy5iDonYsWOHqlWrptSpUytp0qTKli2b3n777Xj5ewDgRcSWdACApAdbIVevXq1y5copc+bM/zj9kiVLJEktW7b8z8+dLFky1atXTz/88IM6d+4sSfrjjz904MABffvtt9q7d+8j84wYMUIDBgxQ48aN1b59e4WGhurzzz9XuXLltHv3br300kv2acPCwlS9enU1aNBAjRs31vz58/XBBx+oQIECqlGjxhNzNWzYUAcOHNB7772nrFmz6tKlS1q1apXOnDnzxF18HV2OMaZOnaq7d++qY8eO9uPXY8ryw/bu3avXXntNbm5u6tixo7Jmzarjx4/rp59+0ogRIx772MePH9frr7+uVKlSadWqVUqdOrVu376t8uXL66+//lKnTp2UOXNmbd68WYGBgbpw4YLGjRunNGnS6KuvvlLnzp31xhtvqEGDBpKkggULPvHviCnbGzduVM6cOSU9KOKlSpVSyZIl5ebmps2bN6tu3br2cV5eXipUqJCkB8V1yJAhqly5sjp37qzDhw/rq6++0vbt27Vp06ZYu/5fuXJFNWrUUNOmTfXWW28pXbp0j810584dVapUSWfOnFG3bt3k5+en6dOna82aNf+0WiRJP/30k7Jnz67SpUs/0/SOaty4sbJmzaqgoCBt3bpVEyZMUFhYmL7//vtnmv9ZTxB4584dVahQQceOHdO7776rbNmyad68eWrTpo2uXbtm/6Fh1apVatasmSpVqqRRo0ZJkg4dOqRNmzape/fuKleunLp166YJEyaof//+yps3ryQpb968unTpkqpWrao0adKoX79+eumll3Tq1CktXLjwXywZAEikDAAgUZo6daqRZLZv326MMeaPP/4wkkz37t2faf433njDSDJhYWH/OsPatWuNJDNv3jyzdOlSY7PZzJkzZ4wxxvTt29dkz57dGGNM+fLlTf78+e3znTp1yri6upoRI0bEerx9+/aZJEmSxBpevnx5I8l8//339mERERHG19fXNGzY8InZwsLCjCQzevRoh/4mR5fjyZMnjSTj7e1tLl269NhxU6dOtQ8rV66c8fLyMqdPn441bXR0tP3/Bw0aZCSZ0NBQc+jQIePn52dKlChhrl69ap9m2LBhJnny5ObIkSOxHqdfv37G1dXVvh5CQ0ONJDNo0KBn+nvCw8ONq6uradeunX1Y7ty5zZAhQ4wxxrz66qumb9++9nFp0qQxVapUMcYYc+nSJePu7m6qVq1qoqKi7NN88cUXRpKZMmWKfVjMev36668fyVC+fHlTvnx5+/1x48YZSWbu3Ln2Ybdu3TI5c+Y0kszatWuf+Pdcv37dSDL16tV7pr//cessxt+XY8x6qlu3bqzpunTpYiSZP/7446nP1bp1ayPpqbeuXbvap49ZDjNmzLAPi4yMNAEBASZFihQmPDzcGGNM9+7djbe3t7l///4Tn3vevHmPXXaLFi2K9bkCAHAcu7sDACRJ4eHhkvTY3bPjYvp/UrVqVaVKlUqzZ8+WMUazZ89Ws2bNHjvtwoULFR0drcaNG+vy5cv2m6+vr3LlyqW1a9fGmj5FihSxTkrn7u6uV199VSdOnHhinqRJk8rd3V3r1q1z6Hj4f7tcGjZsaN+1/ElCQ0O1YcMGvf32249spbfZbI9Mv3//fpUvX15Zs2bVr7/+qpQpU9rHzZs3T6+99ppSpkwZaxlWrlxZUVFR2rBhg0P5Y3h5ealgwYL2Y88vX76sw4cP27dClylTxr6L+5EjRxQaGmrf+v7rr78qMjJSPXr0kIvL/76idOjQQd7e3o8c9+3h4RHrJHRPsnz5cqVPn15vvvmmfViyZMnUsWPHf5w3rl/nj9O1a9dY99977z1JD3L/E09PT61ateqxt79bvny5fH19Y72v3Nzc1K1bN928eVPr16+XJL300ku6devWYx/jn8TswbJ06VLdu3fP4fkBAOzuDgD4f97e3pKkGzduODz9w7uW/1tubm5q1KiRZs2apVdffVVnz55V8+bNHzvt0aNHZYxRrly5nvhYD8uYMeMjJTZlypSP3Y0+hoeHh0aNGqXevXsrXbp0KlWqlGrXrq1WrVrJ19f3ifM5uhxjZMuW7R+niflR4VkvR1enTh2lS5dOK1eufORSXUePHtXevXuf+MPApUuXnuk5Hqds2bL6/PPPdfnyZW3evFmurq4qVaqUJKl06dL68ssvFRER8cjx6KdPn5Yk5c6dO9bjubu7K3v27PbxMTJkyCB3d/d/zBNzPP7fXwN/f57H+bfr0xF/fx3nyJFDLi4uz3R5M1dXV1WuXPmZnuf06dPKlStXrB9AJNl3V49Zvl26dNHcuXNVo0YNZciQQVWrVlXjxo1VvXr1f3yO8uXLq2HDhhoyZIg+++wzVahQQfXr11fz5s3l4eHxTDkBILFjSzoAQNKDk18lSZJE+/bte6bp8+TJI0nPPP2zaN68ufbs2aPBgwerUKFCypcv32Oni46Ols1m04oVKx67BXHSpEmxpn/SieeMMU/N06NHDx05ckRBQUHy9PTUgAEDlDdvXu3evfuJ8zi6HGMkTZrUoemfRcOGDXX8+HHNnDnzkXHR0dGqUqXKE7fCPu5kgM8qpnRv2rRJmzZtUoECBew/EpQuXVoRERHavn27Nm7cqCRJktgLvKPiY5n9nbe3t/z8/J56Nv6HPW6PBkmKiop65ud80mMklLRp02rPnj1asmSJ6tatq7Vr16pGjRpq3br1P85rs9k0f/58bdmyRe+++67++usvvf322ypWrJhu3ryZAOkB4PlHSQcASHqw++/rr7+uDRs2PHKG9MeJua71jBkz4ixD2bJllTlzZq1bt+6JW9GlB1sajTHKli2bKleu/Mjt35a+Jz1X79699csvv2j//v2KjIzUmDFjnji9o8vREdmzZ5ekZy6Mo0ePVrt27dSlSxfNmjUr1rgcOXLo5s2bj11+lStXtu9O/28K48Mnj9u0aZPKlCljH+fn56csWbLYC3yRIkXsl03LkiWLpAeXbHtYZGSkTp48aR/vqCxZsuj48eOP/Cjz9+d5ktq1a+v48ePasmXLP04bc0jB389G//e9AB529OjRWPePHTum6OjoOL/+eJYsWXT06NFHTkj4559/2sfHcHd3V506dfTll1/q+PHj6tSpk77//nv7Wfv/6XVRqlQpjRgxQjt27NDMmTN14MABzZ49O07/HgB4UVHSAQB2gwYNkjFGLVu2fOxWr507d9ov1xQQEKDq1avr22+/1eLFix+ZNjIyUn369HHo+W02myZMmKBBgwY99azxDRo0kKurq4YMGfJI8TLG6MqVKw497+Pcvn37kctg5ciRQ15eXv946S5HlqMj0qRJo3LlymnKlCk6c+ZMrHGP2yvAZrNp8uTJevPNN9W6dWv7GfmlB2cU37Jli1auXPnIfNeuXdP9+/clyV6g/146n8bPz0/ZsmXT6tWrtWPHjkfOil66dGktXrxYhw8fjnXptcqVK8vd3V0TJkyI9fd89913un79umrVqvXMGR5Ws2ZNnT9/XvPnz7cPu337tiZPnvxM87///vtKnjy52rdvb7983cOOHz9uvzyZt7e3UqdO/cgx/V9++eUTH3/ixImx7n/++eeS9NQrD/wbNWvWVEhIiObMmWMfdv/+fX3++edKkSKFypcvL0mPvH9cXFzsZ/SPee0nT55c0qOvi7CwsEdei4ULF441LwDg6TgmHQBgV7p0aU2cOFFdunRRnjx51LJlS+XKlUs3btzQunXrtGTJEg0fPtw+/ffff6+qVauqQYMGqlOnjipVqqTkyZPr6NGjmj17ti5cuPDM10qPUa9ePdWrV++p0+TIkUPDhw9XYGCgTp06pfr168vLy0snT57UokWL1LFjR4d/IPi7I0eOqFKlSmrcuLHy5cunJEmSaNGiRbp48aKaNm361HkdXY6O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+0uSXn75Zd28eVMZM2aUn5+fM2MmSunSpdPnn3+uVq1aaf78+erXr5/Sp0+vw4cPa+bMmerQoYOzIyKBFSxYUMuXL9fcuXOVOnVqLV++XJ988onCwsLsx6AbY5QtWzZ17NjRfh//+/fi8uXL2r59u7799lulSJFC/fv316BBgyRJe/fuVZcuXeTl5aUePXpI0ot3PHUcstlsunXrlv744w81a9ZMktSuXTtVrVpV77//vj788ENlzZpVRYsWVa5cuZycNu5w4rgX2J07d1SqVCn5+/tr5syZscYtXbpUu3btUt++fZU0aVL7SX3w4tu0aZNGjRql0NBQZcmSRfnz59eGDRt0/PhxnThxwtnxnmtXrlzR+vXrtWDBAu3atUv58+dXYGCgihUr5uxoiANNmjTRkCFDlCdPHknShQsXVK5cORUrVkylS5fWl19+qfr162vkyJEv5klsHBRzssqQkBClSpUq1klLmzdvrr1792rKlClaunSpxo8fr9DQUE5smgBiXptnzpzRr7/+KhcXF7388suqU6eOfZqff/5ZkydPlqurq+bPn+/EtHCWyMhIubu7KyIiQp9//rmGDRsmPz8/DR8+XHXr1uUH58eIeW/duXNHb775po4ePaqUKVNq+/bt+u6779S2bVsZY7RkyRKtXr1arVq1UvHixe2flfif69evK1myZLFeZ1u2bNGdO3dUrFgxValSRYMHD1bNmjV1+fJlde3aVV26dFH58uWdmDqOOXMzPuLfL7/8YrJkyWKaN29ufvvtN2OMMVeuXDGNGjUyDRo0cHI6xKeYXaeio6PNn3/+afbv32/fhfHo0aNm1KhRpk6dOiZr1qymV69eZufOnc6M+9z5+659ERER9v8/cuSImThxoqlRo4bJkyeP6dSpE7u5P+dOnTplXnnlFXP48GFjzIP1HxUVZaZOnWoqV65sXnnlFdOsWTP79Il918+H//7KlSubDh06mJCQEPuw06dPm4CAAGOz2Uzx4sVNcHCwM2ImOjGHt+3du9eUKFHC5MqVy9StW9e4u7ubyZMn26ebP3++6du3rwkNDXVWVDhBzPmMfvnlF/P555+bI0eO2MedP3/etGrVynh4eJgyZcqY/fv3OyumZcV872rZsqWpWrWq+euvv8yhQ4eMi4uL2bBhgzHGmAsXLhhjDMfx/4NixYqZcePGPXbctWvXjL+/v3nvvfeMMcbMmzfPpEmT5oU7Jp0t6S8Q85jrBEZHR2vatGmaO3eujh8/Ljc3N7m7u+vChQvasWOHMmbMyBafF1TML7ODBw/WggULdODAAZUsWVL16tVTkyZNlC1bNmdHfK7FvG82btyoNWvW6OLFi8qePbt69+5tn2bbtm2aP3++kiRJoo8//tiJaeGokJAQpUuXLtZnavny5dWiRQt17Ngx1uft2bNn5ePjI3d3d3l6erJVRP/7/Bk+fLjmzJmjuXPnKm/evLHGSQ+uFezj46PMmTM7M26iU7JkSRUqVEiTJ0/WrFmz1LNnT+3cuVMZM2bU9u3bVaJECUVERMjDw8PZUZFAYv5Nu3fvnrJkyaJevXrprbfekq+vb6zXwtatW9WpUyd9+umnqlKlipNTW89ff/2l0qVL2y+tVqVKFWXIkEHBwcG6cuWKevTooaZNm6pWrVrOjmppO3bsUP78+ZU0aVIFBQWpWbNmsS4T/Mknn2jOnDm6fPmy7t+/r969e6tXr17OCxwPKOkvoNWrV2vTpk3Kly+f/XbkyBH9/vvvOnTokPz8/FShQgX5+/vzZfIFFVMgjh07pvz582vKlCnKnTu3pkyZorVr1ypbtmx68803VaFCBWXPnt3ZcZ87Me+b/fv3q2HDhnr55ZdVokQJTZ48WVmyZNGHH36oli1bSpJu3bqlJEmS8GX3ORIVFSVfX1+9/vrrGjFihLJnzy4XFxd98MEHOnnyZKzzDURHR+unn35Snjx5uJ7039y9e1f58uXT0KFD9dZbb0n6XxGIjIzUrVu3lDJlSienTHz++OMPNWnSRL/99pvSpEmjPHnyqHXr1goMDNS5c+f06aefql69eqpYsaKzoyIBxbw3u3btqgMHDmjdunUyxujo0aMKCgrS+fPnNWjQIJUuXdrZUS3n4Y1dV69eVY0aNTR79mz99ddfql+/vnbs2KGsWbPq+vXrql+/vtq1a2f/TMSj7t27Z9/N/ejRoypYsKBeeuklBQYGqk2bNvL29taVK1f0448/KiwsTJkzZ1ajRo2cnDoeOG8jPuJSzC5s06dPNxkyZDDZs2c3KVOmNGXKlDGjR482p06dcnJCOMO0adPMu+++G2vY5s2bTb169Yy/v7+pW7euOXDggJPSPf/KlCljOnXqZIwxZtGiRSZlypSmUaNGxt3d3dSuXdt+iEli3/X5eTR//nxTsGBB4+3tbYYOHWrCw8PN7Nmzzeuvv27Wr19vJkyYYFq1amXSp09vUqdOza6f/+/hq4VcvHjRBAQEmHnz5tmHxbwX9u/fb+rXr2+2bt2a4BkTu2PHjpncuXOb06dPm08++cTkzp3b3Lp1yxjz4CzU+fLlM6tXr3ZySjjDtWvXTNGiRc2sWbOMMcbMnDnTVK1a1ZQsWdJUq1bNlCxZ0v5awaOio6NNZGSkqVmzpunZs6fJli2bGT58uH18cHCwSZ8+Pd8JnuLbb781o0aNMn/99Zd9Od28edMMGjTIfmWqn376yckpEwYl/QVTuHBh+zEc586dM+3bt7cfczZ16lRz+vRpJydEfIv5UNuxY4dp166dqVat2mOPfQoODjbVq1fnEnz/0pYtW0yBAgXsx9kWKFDADB8+3Fy9etVUr17d2Gw2kytXLienxH8RGRlpxo4da1KmTGn8/f3NJ598Yvz8/Iy3t7epVKmS6dWrl1mwYIE5e/asMYZL6PxdRESEKVu2rHnjjTfM5cuXY43bvHmz8fX1jXWcOuLHtm3bYt2/c+eOefPNN023bt1M6tSpzbJly+zjevfubYoVK5bQEWEhbdq0MfXq1TOjR482/v7+ZsiQISYsLMxs2LDBFC9e3Bw8eNDZES1j8eLFJlmyZGb+/Pmxhq9Zs8YUKVLEpEyZ0kyaNMn88ccfZsqUKSZz5szm66+/Nsb87/h/xNa7d29js9lM2bJlzZIlS2KdF+PkyZOmSZMmxmazmQYNGrzw51KipL8AYkrWwYMHTZs2bWKd6MOYBx8WderUMb6+vmb06NHOiAgnGDVqlEmaNKlxd3c3w4cPf+y1uykV/96OHTtMp06dzNWrV838+fNN/vz57dd4/vbbb03Pnj3t5Q3Pt5CQENO2bVvj7u5ukiZNaqZOncp75282b95sSpcubSIjI+0/FEZFRZlZs2YZX19f895775lNmzaZixcvmq1bt5qCBQuabt26OTn1i++zzz4zb7/9tjEm9h49a9asMZkyZTI2m83MnDnT/PTTTyYwMNCkTZvWbNq0yVlxYQE//PCDCQgIMPny5TMff/yx/Uf+BQsWmCxZsnAS1IccO3bMtG7d2iRNmtSUK1fO7Nmzxz5u9erV5rXXXjP58uUzPj4+pkiRIrGuk44nO3v2rKlWrZpJkiSJ6dq1q9myZUusPTjWrVtnChUqZNzc3My1a9ecmDR+UdJfEFevXjWvvfaaSZMmjZkwYcJjp/n6669jnZkYL77jx4+bpk2bGj8/P9OsWTOzePFic+XKFWfHem7FfDmJ2Sp4/fp1Y8yDw0xKly5t/2W8X79+pkWLFs4JiXize/duU7VqVePm5ma6dOlijh496uxIlrFu3Tr7Gdq3bdtm/8HKGGO++eYb4+fnZ3LmzGmyZs1q/Pz8TP369Z0VNVFZt26dOXnypDHGmE8//dSMHTvW/mX3zJkzpnXr1sbNzc1ky5bNVK9e3UyfPt2JaWEVt2/fjlV+Dh06ZLJnz27Gjh1rjDHsgfeQu3fvmvXr15vKlSsbm81m3n777VjLbvXq1ebAgQP2s7obwwaSJ4mKirJ/jzp58qQpU6aMsdlsJlWqVOajjz4yhw8fjvUj0fbt250VNUFw4rgXgDFGd+7cUffu3fXTTz8pbdq06tGjh6pUqaJMmTI5Ox4sYOnSpRo+fLiuXr2q2rVrq27duipfvvwjVwPAo2JOCHPz5k2lSJFC169fV8WKFbVkyRJlzJhR0oNrd1atWlU1a9ZU7ty5NXr0aK1cuVLlypVzcno46v79+0qSJIkOHDigX375RTabTQUKFFCBAgWUNm1aSdKcOXPUuXNn5c2bV5s2bXJyYutp1KiRFi5cqIEDB2rQoEGSHryPpk6dqrRp0yplypQqVKiQvLy8nJw08bh8+bI6dOig8+fPK3v27GrRooVq164tSbpx44ZOnTqlAgUKODklElrMSVDXr1+vWbNmaefOnUqfPr3Kly+vnj17ytXVVZs2bdKECRMUERGhxYsXOzuyZV27dk3Lli3T0KFDdf78eQ0YMEDvv/++s2M9V2Jej7NmzdLgwYP13nvvKW/evNq8ebNGjRqlzJkzKzAwUBUqVFCmTJle+O+wlPQXzP79+9W/f3/t2bNHFStWVNOmTVWqVCnOoJsImP8/o/ulS5e0adMmpU2bVu7u7ipWrJj9rKMTJkzQgAED9O6772rEiBFOTvx8eeutt1SnTh1Nnz5dUVFR+vnnn+2Fzhij4OBgTZ8+XXfu3FGDBg3Ut29fZ0eGg2LeQxEREXrllVeUKlUqnT59WmnTplWlSpVUt25dvfbaa0qWLJkiIiJ0/vx5ZcuWjatk6H8/Zh04cEAXL17U1q1bNXnyZLm6umro0KFq0aKFsyMmKrt27VLPnj01bNgw+4+F58+f18KFC/Xzzz/rypUrevXVV9W6dWsVK1bMPp95zKVc8WKKec/euHFDr7zyilq0aKG8efNq1KhRKlCggBYsWKDo6GjZbDb99ttvyp49uzJmzMjn3UP+/n65f/++QkJCNGXKFI0dO1a+vr4aPXq06tSp48SUz58CBQqoefPmCgwMtA+7cOGCGjdurB07dqhw4cJauHCh0qdP78SU8Y+S/gJ5+INz3rx5CgoKUkREhMqXL6+BAwfK19fXyQkRX2LW/b59+9SxY0edPHlSSZMmVZYsWfT666+rbt26Kly4sCTpypUrcnd3ZyuWA/bt26ePPvpIx48f1+HDhzVlyhT7JdYe/kc6LCxMPj4+stlsfNF9jg0bNkzr1q3TkiVLlDx5ck2cOFFTpkxRkiRJVLt2bVWqVInLED3k4R8IK1asqAULFihDhgzau3evpk2bpvnz56tgwYIaO3asihYt6uy4icKPP/6o8ePH6+LFiypdurQCAwPtl9vct2+f5syZo40bN8rV1VWlS5dWt27dlCZNGienRkKKed927txZx44d06pVqxQaGqps2bJp1apVCggI0M8//yx3d3dVqlTJ2XEt686dO9q9e7dy5cplfw9FR0frwIEDGjNmjL7//nvNmTPnxbxEWDy4ffu26tatq4CAAA0bNkxRUVG6f/++PDw8NHnyZH3//ffKkyePvv32W2dHjXcuzg6AfycqKkqSdOjQIY0dO1atW7fWpEmTtHHjRkkPdjfctWuX3nzzTf35558U9BdczI8z7du3V548eRQSEqIPP/xQv/32m2bOnKmePXtq8uTJOnbsmF5++WWlSJHCyYmfLwUKFNCMGTPk4uIiPz8/ffPNN+revbv27t0bq4wvWLBA4eHhFPTnUMxn6u3btxUVFaWmTZsqefLkkqSuXbtq5cqVqlChgr7//nsNGDBAN27ccGZcy4iKirK/3oODg5UlSxblyZNHXl5eKlOmjEaMGKEpU6YoRYoUKl68uKZNm+bkxIlDvXr19MUXX6hVq1b666+/VKdOHY0fP16RkZEqUKCAhg8frg8//FCvvPKK5s+fr5MnTzo7MhJIzLY5m82mu3fvKiwszH7oQ5MmTdSoUSMFBATo/v372rNnjxYuXKiIiAhnRrac+/fvS5J+/vln1ahRQ2+99Zb8/PzUvXt3HTp0SC4uLipQoIC+/vprbdiwgYLugGTJkumVV17RtGnTdOzYMbm6usrDw0OSVLp0aeXIkUNffPGFk1MmDLakP4difv00xihv3rzKlCmTfHx8tHXrVuXMmVNVq1ZV/fr1lS9fPklSRESEPDw82EXpBbdixQp17dpVe/fuVfLkyZU/f361b99eRYoUUaNGjZQsWTI1bNhQY8eOdXbU50rM+8YYo7lz59q/1G7cuFE2m0116tRRq1attHTpUnXs2FH37t1zdmT8B507d9bSpUtVoEABzZkz55E9TrZt26Zjx46pefPm7Br8kHPnzmnlypX2rUd/Xy4nTpzQr7/+qqZNm8rb29tJKROHh0vY0qVL9cMPP2ju3LlKkSKF8ufPr65du6pZs2aSpFu3bmnr1q1sKU2EYv5t++ijj3T79m3Vrl1bjRs31u7du5UpUyYZY1SmTBnVrl1b/fv35/Pu/z28HDJlyqQWLVqoa9eu6t+/v2bOnKnkyZOrb9++6tSpk9KlS/fY+fB0d+7cUf369XXkyBG1aNFCffr00f79+zVixAgZY7RixQpnR0wYCXN+OsSlmLNC9ujRw5QpU8Y+3MPDw1SuXNm89NJLpnbt2mbs2LEmNDSUM7m/4GLOsjpz5kz7JY0mT55sChYsaK5evWqMMaZJkyamQYMG5rfffnNazufRw++dBQsWxDpj6y+//GI6dOhgSpYsabJkyWJ8fX3NrFmznBETcWjKlCmmRIkSxsfHx/Tu3dts3779idezTcyfrStXrjRNmza1n2m3TZs2xmazmTRp0phdu3Y9dh7OaJwwYpbz8ePHTaZMmcyYMWPMunXrzBdffGGaNm1qMmfObFq0aGF27Njh5KRIaEOGDDHLli2LNWzlypXmpZdeMjabzQwbNswY8+DKJRMmTDCpUqWyT5eYP+8eFrMchg0bZkqUKGGMMebKlSsmVapUZuHChWbQoEHGZrMZPz8/s3LlSmdGfS7EfF7FLNeYq0+cPXvWDBgwwOTNm9e4urqajBkzmldffdVcvHjRaVkTGiX9OfLwB+Tly5eNv7+/+emnn4wxxjRs2NA0atTIGGPMRx99ZLy8vEzx4sUT1Ys5sVm4cKH9/6Ojo83ly5fNH3/8YYwxplu3bqZVq1b210yPHj3Mt99+65Scz7OYH0D69+9v8ufPb5YvXx5rfEREhFmxYoUJDg42S5YscUZExIP79++bIUOGmMyZM5syZcqYiRMnmmPHjjk7lqXkzZvXjBo1yhhjzKlTp8zly5fNlClTjK+vr8mcObOZOXOmuXv3rpNTJm4dOnQwNWvWjDXs8OHD9h9UvL29zZw5c5yUDgnt8OHD5tVXXzVlypQxvXr1Mvv27bOPW758uSlYsKB5+eWXTdu2bY2/v78pWrSomTlzpjHGPPGHysQi5rtAaGio/X7Xrl3N5MmTjTHGdOzY0dSrV88Y8+BydUWKFDGNGzc2Bw8edEre59Gnn35qKlasaFq1amXGjx9vv4xnSEiI2bRpk9m8efMLfU30x6GkP4fu379vQkJCzKhRo8zBgwfN0aNHTa5cucy2bduMMcb8/PPPpmXLluaXX34xxrD14kX0448/GpvNZipWrBjrOpExX4q/+OILky9fPrNgwQIza9Ys4+HhYbZu3eqsuM+lmPfNmTNnTLJkycz69evt46ZPn25GjRplf4/h+fW0rUMnTpwwzZs3N1myZDGVK1c2v/76awIms64TJ06Y3Llzm+nTp5v79++bEiVKmD179hhjHnyheuedd4yrq6upVKmS2bJli5PTJk5RUVGmV69epmzZsrGuK2zMg/VXtmxZM2zYMBMREeGkhHCGHTt2mMDAQFO9enXz+uuvm/Hjx9uL59mzZ82IESNMgwYNzNChQ1/4a1A76v79+yZt2rRm5MiRxhhjdu7caTZs2GBu3bplypYtayZNmmSf9s0337TvUcQeCE8W8z3ru+++M2nSpDHt27c31atXNyVKlDC1a9c2U6dONWFhYc4N6USU9OdEhw4dzA8//GC/f//+fXPu3Dlz7949s3XrVpMnTx6zZs0aY4wxS5YsMWXKlLH/8scHxIsnNDTULFq0yNSpU8d4eXmZ1q1bmytXrtjH79ixw5QtW9ZkyZLF5MyZ03Tv3t15YZ9DD/+w1b9/f1OtWjVjjDHnzp0zQ4YMMS+99JLJlSuX8fPzMwcOHHBWTPxHMev57t27Zt68eaZ+/fpm+PDhZu7cubH2Qvr1119NkSJFzM6dO50V1VKioqJM+/btTbly5Uy5cuVMzpw5H5lm165dplq1asZms5lx48Y5ISXWrFljcuXKZYKDg2N90b169aqpVKmS2bhxo/PCIcHFfCe8e/euGTBggEmfPr1Jnjy5qVu37lP3qOA75AMRERGmb9++JmfOnGbMmDEmOjraREdHm6ioKPP666+b9u3bm7t375rvvvvOeHt7m/DwcGdHfm40btw41o8cCxYsMA0bNjSvvvqqad26daLd44cTxz0HwsLC1KFDB61Zs0bFixfX2LFj5e/vbx9/8eJF1a5dWwULFpS3t7fmzZunrl27KjAw0H4dTLyYTp8+rZUrV+qrr77SuXPn1KdPH33wwQeSpMjISP3yyy8qUKCAMmTIoCRJkjg57fPpq6++0ldffaX169erS5cuioyMVKtWrVSvXj0FBASoY8eOatu2rbNj4l+I+Xxs3769du7cqbx58+rPP//UrVu3VKFCBb3xxht6/fXX5e7ubp/HcPIfSdK1a9fUrl07LVu2TGXLllXHjh1VtmxZ+fn5xZpu7ty5KlasmHLkyOGkpInXtWvX1KNHD/38889q2bKlKleuLBcXFy1dulSLFi3S2bNnnR0RCSjm865Dhw66ceOG8ubNq3v37mnbtm0KDQ1V8eLF9fbbbysgIMDZUS3rwoULGjp0qJYsWaLhw4fb/+2fNm2aOnfuLFdXV6VOnVpdu3ZVnz59OGHzU9y/f19JkiTR1q1b9eWXX+qNN97QG2+8YR9/48YNTZ8+XVOnTlVAQIAmTJjgxLRO4uQfCfCMLly4YBYsWGAqVapkvLy8TOfOne0nVzDGmBkzZpiSJUuaSpUqmR49ejgxKRLCw79sR0REmF27dpkBAwaYjBkzmty5c5t58+Y5Md3za+3ataZLly6xtqQfO3bMZM2a1Xh5eZncuXObHTt22HcfzZs3r5k2bZqz4uI/iFnHu3fvNt7e3vaTaFWpUsUULVrU5MyZ0+TJk8e8//779i2ObFF6IGY5NGvWzBQpUsTUqFHD5M+f33Tu3Nn8/PPPsf5tQsJ4+LUZFRVlbt68ab8/efJkkyNHDuPv729SpEhhypYta9/zDolDzOtj9+7dxt3d3Rw9etQ+7ujRo+a9994zbm5uJn/+/KZfv3581v2DXr16GZvNZj766CP7vyVHjx41kydPjnWID8sxtphldePGDWPMg3MdFC9e3Hh6epo33njDfujFw44cOWJCQkISNKdVsCX9OWKM0bFjx7RixQpNmjRJV65cUb9+/dS9e3dJ0t27d3X37l299NJLksQveC8o89CWvIf/PywsTH/88YeCg4O1bNky5cyZU9OnT1fOnDmdGfe5Mm7cOPn6+qpp06batWuXvLy8lCtXLt29e1e7d+9WxowZlSlTJt26dUtffPGFvvzyS50+fdrZsfEfdOrUSREREQoODtaiRYvUuXNnnTx5UqdPn1a5cuXk5uamzz77TI0bN3Z2VEubOHGipkyZoiRJkqhmzZqqXr26SpYs6exYiUbMv/eTJk3SqlWrtGvXLtWsWVMDBgxQunTpFB0dra1btyp16tRKmTKl0qRJ4+zIcIKFCxeqT58+WrFihV555ZVY3yGqVq2q27dvq2/fvqpXr16i32soZs+DgwcP6uzZs6pWrZpu376tZMmSSZJGjhyp4OBgtWzZUt26dXvkcp2Jffk9SXR0tBo3bqxSpUqpW7du2r17t7788kutXbtW5cuXV4MGDVS9enUlTZrU2VGdjpL+HPh72b5z544OHjyouXPn6vvvv1fq1Kn1ySefqEaNGk5MiYTw8If+6tWrtX37dt25c0e9e/e2X3v4/Pnz2rx5s0aOHKnhw4erevXqzoz8XIqOjlaNGjV0+/ZttWzZUi1atFDy5MklPXj/TZw4UZMmTdL48eNVs2ZNJ6fFvxUVFaUFCxYoKipKzZo1U+3atVWsWDENGTJE4eHh6tSpkypVqqT27ds7O6pTxXzu3Lt3T7du3bL/EPx3oaGhGjVqlH7++We5ublpxowZsQ7NQvyIWT+HDh1S8eLF1bx5c6VPn15z5szRhQsX9P7776t///4c+gZdunRJFStWVNu2bdWtWze5ubnZv1P069dPqVOnVp8+fZyc0lqyZMmis2fPqlSpUqpZs6Y8PT1VpUoVFSpUSL169dLcuXM1cOBAdezY0dlRnwuhoaF65513FBISovTp0+u9995T+fLltWjRIo0bN0537txRhQoVVLt2bZUrV87ZcZ2Kkv6cOHbsmBo3bqzvvvtORYoUkSRdvXpVO3fuVHBwsBYuXKjKlStr8eLFbD1/gcX8YDN48GDNmTNHGTJk0KVLl3T69Gn16tVLAwYMkIuLi6KiohQSEqIMGTI4O/Jz4+/nb5g7d66WLVumP//8U1myZFHLli1Vp04dSdKGDRsUGhqqhg0bOisu4sjNmzcVEREhb29v1atXT/ny5dOnn36q6Oho5cuXT9OmTVPJkiXZKiKpefPmkh6cB+XNN9+Ui4uLihUrpsyZMys6Olq+vr6SpKNHj2r69OkaOnSoM+MmOiNGjND58+c1ceJESQ++I3zzzTcaOXKk0qdPrwEDBqhZs2ZOTglniYqKkjFGQ4cO1SeffKIuXbqoY8eOSpYsma5du6Zy5copODhY9evX5/NO//vxa8yYMVq8eLFSp06tTJky6c6dO1qyZImKFi2qZs2aacKECdq1a5f69eunESNGJPrl9iyio6O1du1ajR8/XufPn1fp0qXVs2dP+fr66osvvtC8efN09+5dTZkyRcWLF3d2XKehpD8ndu3apeLFi8vFxUWtWrXSJ598otSpU0uSzp07p5UrVyo6OlodOnTgw/UFFVMiT506JX9/fy1ZskSvv/66GjRooEOHDik0NFSpUqXSyJEj1aBBA2fHfe7ELN8LFy7o9OnTKlWqlC5fvqy5c+dq+fLlunLliooXL64OHTqoYMGCzo6LeNCnTx9t2rRJZcuW1a5du3T16lXt3r3b2bEs4ezZsypUqJA6deqkXLlyadGiRXJzc9OuXbvk6uqql19+WT4+PipXrpy8vLzUo0cPZ0dOFGJ+uN23b582b96s06dPa/jw4bF+cDx58qQGDBigX3/9VefPn2eLOjRr1iz16dNH9+/f18svv6xbt26pePHiWrhwobOjWc6tW7f09ddf6+TJk2rZsqVKliypK1euaPz48Tpx4oSMMfrhhx/UpUsXffHFF86O+1y5c+eOpk+frlmzZikyMlINGjRQ586ddenSJX3//fcaNGiQsyM6FSXdwmLOfLh06VJ99dVXSpEihTw9PbVx40aFhIRowIAB6tevn31am80mV1dXSvoLrkePHgoNDdXMmTO1detW1ahRQ7/99ptOnz5t39I7evRo9e7d28lJnx8Pb0Vv1qyZ0qZNq/Hjx9vH//nnn/rhhx+0efNmnTt3Tl988YUqVarkrLiIJydPnlRgYKBOnz6tXLlyKTAwUHnz5uX8Hv8vKChIEydO1E8//aQCBQooKipKUVFRSpEihfr27atLly7pjz/+UKlSpfTll186O26i0qhRIy1YsEC5cuXSxo0b7cecP/x9IDQ0lGPRE5GYf9ciIiL0xx9/6PTp07p//77q1q1rP3xr+vTpioqKUs6cOVWgQAH5+Pjweaf/vW9i/hsWFqb+/ftrzpw5mjhxon2PlPDwcIWFhenq1asqWLCgXF1duarSvxASEqLx48dr7dq18vHxUatWrdSiRQtnx3I6SvpzIEOGDOrbt6+6d+8uY4xOnz6tyZMna9SoUSpcuLCGDRumWrVqOTsmEsDdu3f12WefKXXq1OrQoYPq1q2rbNmyafz48QoLC1O3bt305ptvqmbNmnJzc3N23OfC3/9BnTJlimbPnq2VK1fKGBNr3Nq1a7V8+XIFBQVxSbvn0NO+fD5cZq5du2Y/7pofPWMbPny4Dh48qMmTJytFihTq2bOn1qxZo23btsnDw0Ph4eFyd3eXp6ens6O+8G7cuGE/WVVISIiWLVumYcOG6e7duxo9erRatmwpiddwYhWz3rt27ar169crKipKXl5eSpo0qd5++221bt3a2REtJ2aZnTlzRmfPnlWBAgVks9ns77NJkyZp+vTpatq0qdq0aaMUKVLw/opDe/fu1YcffqgcOXJo3Lhxzo7jdPzUY3F79+6Vh4eHypUrJ5vNJhcXF2XLlk39+/dX3bp1debMGTVo0EDdunXT3bt3nR0X8czT01Pdu3dX+fLlFR0dLWOMXnnlFfu4w4cPy8PDg4L+jDZt2qQ+ffrE2qU5f/78CgkJ0d27dx/5Nbxw4cIaPXo0Bf05NGDAAFWsWFH79u177PiYL1mzZ8/WsGHDFPP7NV++HohZHs2bN9fhw4fVqFEjbd68WRMnTtTIkSPl4eGh6OhoeXt7U9ATwNKlS5U1a1bNnTtX9+/fl6+vr9q2bavVq1eradOm6tChg0qVKqXff/+d13AiFBUVJZvNplWrVmnGjBkKDg62H8ITFhamwYMHq3Hjxtq4caOzo1pKzHtl/Pjxeu2111S6dGn17t1bI0aMUEhIiFq0aKEGDRpo27Zt2r59e6x58N8VLFhQixcv1scff+zsKJZASbe49OnT6+7duwoODo413MvLS02bNlWXLl301VdfadGiRdq5c6dzQiJBJUuWTK+88oru378vDw8PjRgxQrNmzbIfx8PZ3J/d2rVrtXTpUg0aNEgTJkzQuXPn5O/vr9u3b+vcuXOKjIzUzp07NWHCBFWvXl2dO3d2dmT8S1WqVNHNmzdVqlQp9e3bVxcuXHhkmqtXr6pPnz72L7jsaPY/MV9Es2fPrl9//VXe3t6qUqWK3n77bdWoUeORvU4Qv0qWLKmaNWuqVatWql69un7//Xe5uLgoR44cGj16tNavX6/06dMrICDAfiI5JB4xewzFHPpWvHhxLVq0SPfu3dP06dNVrVo1zZ8/X3Xq1NHatWudnNZ63n33XR08eFB16tTRuXPnNGvWLGXIkEHNmzdXaGiotm/frrp162rq1KnOjvrCcXV1tV/mLrHjX1SLS5MmjUaNGqVff/1V/fv31549eyRJERERmj9/vkJDQ9WiRQv5+PhwgqMXUHR0tKQHv4r/9ttvGjNmjAYMGKDTp0/L3d1d48ePV5kyZdShQwdduHBBM2fOdHLi58tHH32kKVOmKFmyZAoODlafPn20fPlyZcyYUQ0aNFDZsmVVo0YNTZ48WcWLF9f777/v7Mj4l8qVK6ddu3bp888/18yZM1W8eHFNnjxZt27dsk/zxRdfKDo6mt3sniI6OlopU6bUm2++KZvNZr+WLVuTElaaNGk0ffp0bdy4UVFRUSpbtqw6d+6sM2fOyM3NTSVLltT06dM1d+5cNW3a1Nlx4QQhISF6+eWXlT9/fknSxx9/rN69e9tPAPn6669rzJgxqlixopOTWk+2bNmUJ08eBQUFadasWVq4cKF++uknubq6atu2bUqTJo1u3bqlFStWODsqXmAck24xjzu25dq1a/rss8+0atUq2Ww2+27v+/fv1969e5UxY0aVKFFCbdu2VZcuXZyUHPEh5njpDz74QKtWrVKaNGl06dIlHThwQMeOHVPmzJlljNGVK1dks9n08ssvOzvyc+Pvx6LH7BJ4584dnTlzRl5eXvr0009VtGhR+6Wl8GK4fv26goKCNG7cOBUqVEgff/yxMmbMqOLFi+ubb75R06ZN7SfuxJPNnz9fAwcOVI8ePfT222+zvJxozpw5CgwMVHh4uPr3768OHTrYj6NF4rB27VplzpxZOXLksA+7fv26bt++rYiICDVq1Eiff/65SpUqpePHj6tjx46aPHmycuTIwXHVjxEdHW3/zv2wY8eO6eLFizp69Khq1qyptGnTcrI9xAtKukXt3LlTW7ZsUaFChVS4cGF5eXlp06ZNWr16tc6fP6/UqVOrSZMmKlCggL777jv17dtXly9fZnfDF0hMiTx48KCKFSumdevWqWTJkqpevbrSpUunadOmKSQkRBcvXlShQoWcHfe59XBZDwsL09dff63Fixfbd+etWrWqChcu7NyQiBdHjhzR+++/rxUrVigqKkrFixfXli1bnB3L8mK+Nty+fVvvv/++ZsyYoSNHjihdunROTpa43b59W2PG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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.columns.tolist())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9opYKUC9sXSS",
        "outputId": "88739eb3-1017-4e54-8f42-4afb3a804f8e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Year', 'Winner']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "success = pd.DataFrame({\n",
        "    \"Titles\": winner_count,\n",
        "    \"Runner-up\": runner_up_count\n",
        "}).fillna(0)\n",
        "\n",
        "success[\"Finals\"] = success[\"Titles\"] + success[\"Runner-up\"]\n",
        "\n",
        "success = success.sort_values(\"Titles\", ascending=False)\n",
        "\n",
        "print(success)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ixy-3vYmsYeu",
        "outputId": "3ead03b0-cf43-47b3-8bb8-14ddeaf48498"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "             Titles  Runner-up  Finals\n",
            "Australia       6.0          2     8.0\n",
            "India           2.0          2     4.0\n",
            "West Indies     2.0          1     3.0\n",
            "England         1.0          3     4.0\n",
            "Pakistan        1.0          1     2.0\n",
            "Sri Lanka       1.0          2     3.0\n",
            "New Zealand     0.0          2     2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10, 6))\n",
        "\n",
        "winner_count.sort_values().plot(kind=\"barh\")\n",
        "\n",
        "plt.title(\"ICC Men's Cricket World Cup Winners\")\n",
        "plt.xlabel(\"Number of Titles\")\n",
        "plt.ylabel(\"Team\")\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 564
        },
        "id": "Vj_SG_0ntMm_",
        "outputId": "dc90677b-f692-4185-df37-62bb83d2d6b3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x600 with 1 Axes>"
            ],
            "image/png": "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1dtvv23uv2zZMj366KPq06ePunfvrnbt2snFxUWHDx/W8uXLlZSUlOd3HWbq2bOnevbsmWufKlWq6O2331ZYWJgSEhLUq1cvubm56ciRI1q9erWef/75fAfTWx06dEjt2rVTv379VLNmTdnZ2Wn16tX6559/9MQTT+Q6Nr/HMT9mzZqlFi1aqEGDBnr++efl5+enhIQEffvtt4qNjc3S38bGRp999pl69eqlfv36af369Wrbtq3GjRuntWvXqlu3bgoJCVHDhg118eJFHThwQCtXrlRCQoL5nXI1a9bUV199papVq6pEiRKqXbv2be97bNGihT799FNJspjNyjw+X375pblfJi8vL4WFhSkiIkKdOnVSjx49FBcXp7lz56px48YWDxXKj+eee04ffvihnnnmGcXExKhcuXL69NNP8/xy9SpVquiLL77Q448/rho1auiZZ55R7dq1deXKFe3YsUNff/21+b2VkvTss89qypQpevbZZ9WoUSP9+OOPOnToUI7rP3LkiHr06KFOnTpp586d+uyzz/Tkk0+aX++RmyZNmsjBwUE7d+5UmzZtLF5q7+zsrLp162rnzp3y9PTM872qBakgfleXLl2quXPnqnfv3qpSpYouXLighQsXyt3dXV26dLlHewKg0N3jp6MCAG5y66ssbhYTE2M8+eSTRvny5Q17e3ujePHiRrt27YylS5davGLAMAwjLS3NmDZtmtG4cWPD1dXVcHBwMAICAowXX3zR4nH42bn5VRa5ufVVFpm++eYbo0WLFoaLi4vh4uJiVK9e3QgNDTXi4uJuO3bgwIGGj49Pjts8ffq0ERoaalSvXt1wcXExPDw8jKZNm1q8DuF28nIcM199kN0rM3J6LcKvv/5q9O7d2/D09DScnJyMatWqGW+88YZ5+c2vssiUlpZmtG7d2nB1dTV27dplGIZhXLhwwQgLCzP8/f0NBwcHo1SpUkZQUJAxbdo048qVK+axO3bsMBo2bGg4ODjk+bUWH330kSHJqFChQpZlP//8syHJkGT8888/WZZ/+OGHRvXq1Q17e3ujTJkyxrBhw7K8MiWn85q57OZXWRiGYRw9etTo0aOH4ezsbJQqVcp46aWXjA0bNtz2VRY3O3TokPHcc88Zvr6+hoODg+Hm5mY0b97cmD17tnH58mVzv7S0NGPIkCGGh4eH4ebmZvTr1884efJkjq+yOHjwoPHYY48Zbm5uRvHixY0RI0YYly5dylNNhmEYzZo1MyQZr732WpZlI0eONCQZnTt3zrIsp1dZhIaGZunr4+NjDBw4MMvYm/+MGcb//XflyJEjFu1387v6888/G/379zcqVapkODo6GqVLlza6detmREdHZ3s8ADyYTIZxmycBAAAAFFHh4eGKiIjQqVOnVKpUKWuXAwBWxT2HAAAAAADCIQAAAACAcAgAAAAAkMQ9hwAAAAAAZg4BAAAAAIRDAAAAAIAku9t3wYMoIyNDx48fl5ubm0wmk7XLAQAAAGAlhmHowoULKl++vGxscp4fJBwWUcePH5e3t7e1ywAAAABwnzh27JgqVqyY43LCYRHl5uYm6cYfAHd3dytXAwAAAMBaUlJS5O3tbc4IOSEcFlGZl5K6u7sTDgEAAADc9nYzHkgDAAAAACAcAgAAAAAIhwAAAAAAEQ4BAAAAACIcAgAAAABEOAQAAAAAiHAIAAAAABDhEAAAAAAgwiEAAAAAQIRDAAAAAIAIhwAAAAAAEQ4BAAAAACIcAgAAAABEOAQAAAAAiHAIAAAAABDhEAAAAAAgyc7aBaBw1Z64UTaOztYuAwAAAHhoJEzpau0S7ggzhwAAAAAAwiEAAAAAgHAIAAAAABDhEAAAAAAgwiEAAAAAQIRDAAAAAIAIhwAAAAAAEQ4BAAAAACIcAgAAAABEOAQAAAAAiHAIAAAAABDhEAAAAAAgwiEAAAAAQIRDqwgPD1e9evXM30NCQtSrVy+r1QMAAAAARSoc7ty5U7a2turatWuBrnfJkiXy9PQs0HXebObMmVqyZEmhrR8AAAAAbqdIhcNFixbpxRdf1I8//qjjx4/f8+1fuXLljsZ5eHgUavgEAAAAgNspMuEwNTVVX331lYYNG6auXbtazMRlN/O3Zs0amUwm8/f9+/crODhYbm5ucnd3V8OGDRUdHa2tW7dq0KBBSk5OlslkkslkUnh4uCTJ19dXb731lp555hm5u7vr+eeflyS9+uqrqlq1qpydnVW5cmW98cYbunr1ao6133pZ6YYNG9SiRQt5enqqZMmS6tatm+Lj4+/6GAEAAABATopMOFyxYoWqV6+uatWq6amnntInn3wiwzDyPH7AgAGqWLGi9u7dq5iYGI0fP1729vYKCgrSjBkz5O7urqSkJCUlJWns2LHmcdOmTVPdunW1b98+vfHGG5IkNzc3LVmyRAcPHtTMmTO1cOFCffDBB3mu5eLFixo9erSio6O1adMm2djYqHfv3srIyMhxTHp6ulJSUiw+AAAAAJBXdtYuoKAsWrRITz31lCSpU6dOSk5O1rZt29SmTZs8jU9MTNS4ceNUvXp1SVJAQIB5mYeHh0wmk8qWLZtlXNu2bTVmzBiLttdff938s6+vr8aOHavly5frlVdeyVMtffv2tfj+ySefyMvLSwcPHlTt2rWzHRMZGamIiIg8rR8AAAAAblUkZg7j4uK0Z88e9e/fX5JkZ2enxx9/XIsWLcrzOkaPHq1nn31W7du315QpU/J8GWejRo2ytH311Vdq3ry5ypYtK1dXV73++utKTEzMcy2HDx9W//79VblyZbm7u8vX11eScl1HWFiYkpOTzZ9jx47leXsAAAAAUCTC4aJFi3Tt2jWVL19ednZ2srOz07x58/TNN98oOTlZNjY2WS4xvfUewPDwcP3222/q2rWrNm/erJo1a2r16tW33baLi4vF9507d2rAgAHq0qWL1q1bp3379mnChAn5elhN9+7ddfbsWS1cuFC7d+/W7t27JeX+wBtHR0e5u7tbfAAAAAAgrx74y0qvXbumZcuWafr06Xr00UctlvXq1UtffvmlfHx8dOHCBV28eNEc5mJjY7Osq2rVqqpatapefvll9e/fX4sXL1bv3r3l4OCg69ev56meHTt2yMfHRxMmTDC3HT16NM/7c+bMGcXFxWnhwoVq2bKlJGn79u15Hg8AAAAAd+KBD4fr1q3TuXPnNGTIEHl4eFgs69u3rxYtWqSNGzfK2dlZr732mkaOHKndu3dbPM300qVLGjdunB577DH5+fnp77//1t69e833/vn6+io1NVWbNm1S3bp15ezsLGdn52zrCQgIUGJiopYvX67GjRvr22+/zdMMZKbixYurZMmSWrBggcqVK6fExESNHz8+/wcGAAAAAPLhgb+sdNGiRWrfvn2WYCjdCIfR0dH6+++/9dlnn2n9+vWqU6eOvvzyS/PrKCTJ1tZWZ86c0TPPPKOqVauqX79+6ty5s/kBL0FBQXrhhRf0+OOPy8vLS++++26O9fTo0UMvv/yyRowYoXr16mnHjh3mp5jmhY2NjZYvX66YmBjVrl1bL7/8st577728HxAAAAAAuAMmIz/ve8ADIyUl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76hmAAAAALidBzIcurq6ytXVVWvWrFF6enqufcPDw9W7d28dOHBAgwcPvuttZ2RkqGLFivr666918OBBvfnmm3rttde0YsUKi35btmxRfHy8tmzZoqVLl2rJkiVasmRJtut89913NX78eP33v/9Vu3btJEk2NjaaNWuWfvvtNy1dulSbN2/WK6+8kmNd6enpSklJsfgAAAAAQF49kOHQzs5OS5Ys0dKlS+Xp6anmzZvrtdde0y+//JKl75NPPqlBgwapcuXKqlSp0l1v297eXhEREWrUqJH8/Pw0YMAADRo0KEs4LF68uD788ENVr15d3bp1U9euXc2zgjd79dVXNWPGDG3btk1NmjQxt48aNUrBwcHy9fVV27Zt9fbbb2fZxs0iIyPl4eFh/nh7e9/1vgIAAAB4eDyQ4VC6cc/h8ePHtXbtWnXq1Elbt25VgwYNsszONWrUqMC3PWfOHDVs2FBeXl5ydXXVggULlJiYaNGnVq1asrW1NX8vV66cTp48adFn+vTpWrhwobZv365atWpZLPvhhx/Url07VahQQW5ubnr66ad15swZpaWlZVtTWFiYkpOTzZ9jx44V0N4CAAAAeBg8sOFQkpycnNShQwe98cYb2rFjh0JCQjRx4kSLPi4uLgW6zeXLl2vs2LEaMmSI/vvf/yo2NlaDBg3SlStXLPrZ29tbfDeZTMrIyLBoa9mypa5fv55lRjAhIUHdunVTYGCgvvnmG8XExGjOnDmSlGU7mRwdHeXu7m7xAQAAAIC8emCfVpqdmjVras2aNYW6jaioKAUFBWn48OHmtvj4+DtaV5MmTTRixAh16tRJdnZ2Gjt2rCQpJiZGGRkZmj59umxsbuT33C4pBQAAAIC79UCGwzNnzuhf//qXBg8erMDAQLm5uSk6OlrvvvuuevbsWSDb+N///qfY2FiLNh8fHwUEBGjZsmXauHGj/Pz89Omnn2rv3r3y8/O7o+0EBQVp/fr16ty5s+zs7DRq1Cj5+/vr6tWrmj17trp3766oqCjNnz+/APYKAAAAALL3QIZDV1dXNW3aVB988IHi4+N19epVeXt767nnntNrr71WINuYNm2apk2bZtH26aefaujQodq3b58ef/xxmUwm9e/fX8OHD9d33313x9tq0aKFvv32W3Xp0kW2trZ68cUX9f7772vq1KkKCwtTq1atFBkZqWee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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "success = pd.DataFrame({\n",
        "    \"Titles\": winner_count,\n",
        "    \"Runner-up\": runner_up_count\n",
        "}).fillna(0)\n",
        "\n",
        "success[\"Finals\"] = success[\"Titles\"] + success[\"Runner-up\"]\n",
        "\n",
        "success = success.sort_values(\"Titles\", ascending=False)\n",
        "\n",
        "print(success)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-phACqGCtXIY",
        "outputId": "89aefb3c-0080-4a53-f392-8860fccb96cd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "             Titles  Runner-up  Finals\n",
            "Australia       6.0          2     8.0\n",
            "India           2.0          2     4.0\n",
            "West Indies     2.0          1     3.0\n",
            "England         1.0          3     4.0\n",
            "Pakistan        1.0          1     2.0\n",
            "Sri Lanka       1.0          2     3.0\n",
            "New Zealand     0.0          2     2.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Find the actual Winner and Runner-up column names\n",
        "winner_col = next(\n",
        "    col for col in world_cup_df.columns\n",
        "    if \"winner\" in col.lower()\n",
        ")\n",
        "\n",
        "runner_up_col = next(\n",
        "    col for col in world_cup_df.columns\n",
        "    if \"runner\" in col.lower()\n",
        ")\n",
        "\n",
        "print(\"Winner column:\", winner_col)\n",
        "print(\"Runner-up column:\", runner_up_col)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HH-0b2GftqId",
        "outputId": "8b42ff15-3825-4b0a-f9f6-ea301fb0e70c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Winner column: Winner\n",
            "Runner-up column: Runner_Up\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "world_cup_results = world_cup_df[\n",
        "    [\"Year\", \"Host\", winner_col, runner_up_col]\n",
        "].copy()\n",
        "\n",
        "world_cup_results.columns = [\n",
        "    \"Year\",\n",
        "    \"Host\",\n",
        "    \"Winner\",\n",
        "    \"Runner-up\"\n",
        "]\n",
        "\n",
        "world_cup_results"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 457
        },
        "id": "AsGFNm0wuDMA",
        "outputId": "3d6120d8-a167-441a-8611-715ef862cb4a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Year                           Host       Winner    Runner-up\n",
              "0   1975                        England  West Indies    Australia\n",
              "1   1979                        England  West Indies      England\n",
              "2   1983                        England        India  West Indies\n",
              "3   1987               India & Pakistan    Australia      England\n",
              "4   1992        Australia & New Zealand     Pakistan      England\n",
              "5   1996    India, Pakistan & Sri Lanka    Sri Lanka    Australia\n",
              "6   1999                        England    Australia     Pakistan\n",
              "7   2003                   South Africa    Australia        India\n",
              "8   2007                    West Indies    Australia    Sri Lanka\n",
              "9   2011  India, Sri Lanka & Bangladesh        India    Sri Lanka\n",
              "10  2015        Australia & New Zealand    Australia  New Zealand\n",
              "11  2019                England & Wales      England  New Zealand\n",
              "12  2023                          India    Australia        India"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-746e4114-13d1-45d6-a349-2cfc3b8e68d2\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Year</th>\n",
              "      <th>Host</th>\n",
              "      <th>Winner</th>\n",
              "      <th>Runner-up</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1975</td>\n",
              "      <td>England</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1979</td>\n",
              "      <td>England</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1983</td>\n",
              "      <td>England</td>\n",
              "      <td>India</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1987</td>\n",
              "      <td>India &amp; Pakistan</td>\n",
              "      <td>Australia</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1992</td>\n",
              "      <td>Australia &amp; New Zealand</td>\n",
              "      <td>Pakistan</td>\n",
              "      <td>England</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>1996</td>\n",
              "      <td>India, Pakistan &amp; Sri Lanka</td>\n",
              "      <td>Sri Lanka</td>\n",
              "      <td>Australia</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>1999</td>\n",
              "      <td>England</td>\n",
              "      <td>Australia</td>\n",
              "      <td>Pakistan</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2003</td>\n",
              "      <td>South Africa</td>\n",
              "      <td>Australia</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>2007</td>\n",
              "      <td>West Indies</td>\n",
              "      <td>Australia</td>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>2011</td>\n",
              "      <td>India, Sri Lanka &amp; Bangladesh</td>\n",
              "      <td>India</td>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>2015</td>\n",
              "      <td>Australia &amp; New Zealand</td>\n",
              "      <td>Australia</td>\n",
              "      <td>New Zealand</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>2019</td>\n",
              "      <td>England &amp; Wales</td>\n",
              "      <td>England</td>\n",
              "      <td>New Zealand</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>2023</td>\n",
              "      <td>India</td>\n",
              "      <td>Australia</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-746e4114-13d1-45d6-a349-2cfc3b8e68d2')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-746e4114-13d1-45d6-a349-2cfc3b8e68d2 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-746e4114-13d1-45d6-a349-2cfc3b8e68d2');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_9fa2d752-ae27-4b9d-bac4-47d694f2fcab\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('world_cup_results')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_9fa2d752-ae27-4b9d-bac4-47d694f2fcab button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('world_cup_results');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "world_cup_results",
              "summary": "{\n  \"name\": \"world_cup_results\",\n  \"rows\": 13,\n  \"fields\": [\n    {\n      \"column\": \"Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15,\n        \"min\": 1975,\n        \"max\": 2023,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          2019,\n          2011,\n          1975\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Host\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 9,\n        \"samples\": [\n          \"England & Wales\",\n          \"India & Pakistan\",\n          \"West Indies\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Winner\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"West Indies\",\n          \"India\",\n          \"England\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Runner-up\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Australia\",\n          \"England\",\n          \"Sri Lanka\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 57
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "winner_count = world_cup_df[winner_col].value_counts()\n",
        "\n",
        "print(winner_count)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "phoeHw7RuNFP",
        "outputId": "8cd84a48-e0b9-4ba7-a07c-9bfebdb3c955"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Winner\n",
            "Australia      6\n",
            "West Indies    2\n",
            "India          2\n",
            "Pakistan       1\n",
            "Sri Lanka      1\n",
            "England        1\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "india_wins = (\n",
        "    world_cup_df[winner_col] == \"India\"\n",
        ").sum()\n",
        "\n",
        "india_runnerups = (\n",
        "    world_cup_df[runner_up_col] == \"India\"\n",
        ").sum()\n",
        "\n",
        "print(\"India World Cup Titles:\", india_wins)\n",
        "print(\"India Runner-up Finishes:\", india_runnerups)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "loTrwP9tuQTA",
        "outputId": "51af69cd-d7c9-45fe-c704-2421378ecf9e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "India World Cup Titles: 2\n",
            "India Runner-up Finishes: 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "india_results = world_cup_df[\n",
        "    (world_cup_df[winner_col] == \"India\") |\n",
        "    (world_cup_df[runner_up_col] == \"India\")\n",
        "]\n",
        "\n",
        "india_results[\n",
        "    [\"Year\", \"Host\", winner_col, runner_up_col]\n",
        "]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "id": "wP-vXcUluZXh",
        "outputId": "1a3bddc5-0992-4f75-90e6-17b963d5ef71"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Year                           Host     Winner    Runner_Up\n",
              "2   1983                        England      India  West Indies\n",
              "7   2003                   South Africa  Australia        India\n",
              "9   2011  India, Sri Lanka & Bangladesh      India    Sri Lanka\n",
              "12  2023                          India  Australia        India"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-561eca1a-7654-499f-a89e-6061cc52ceda\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Year</th>\n",
              "      <th>Host</th>\n",
              "      <th>Winner</th>\n",
              "      <th>Runner_Up</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1983</td>\n",
              "      <td>England</td>\n",
              "      <td>India</td>\n",
              "      <td>West Indies</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2003</td>\n",
              "      <td>South Africa</td>\n",
              "      <td>Australia</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>2011</td>\n",
              "      <td>India, Sri Lanka &amp; Bangladesh</td>\n",
              "      <td>India</td>\n",
              "      <td>Sri Lanka</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>2023</td>\n",
              "      <td>India</td>\n",
              "      <td>Australia</td>\n",
              "      <td>India</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-561eca1a-7654-499f-a89e-6061cc52ceda')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-561eca1a-7654-499f-a89e-6061cc52ceda button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-561eca1a-7654-499f-a89e-6061cc52ceda');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"]\",\n  \"rows\": 4,\n  \"fields\": [\n    {\n      \"column\": \"Year\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 16,\n        \"min\": 1983,\n        \"max\": 2023,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2003,\n          2023,\n          1983\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Host\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"South Africa\",\n          \"India\",\n          \"England\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Winner\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"Australia\",\n          \"India\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Runner_Up\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"West Indies\",\n          \"India\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 60
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"========== WORLD CUP SUMMARY ==========\")\n",
        "\n",
        "print(\"Total World Cups:\", len(world_cup_df))\n",
        "\n",
        "print(\n",
        "    \"Different winning teams:\",\n",
        "    world_cup_df[winner_col].nunique()\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"Different host entries:\",\n",
        "    world_cup_df[\"Host\"].nunique()\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"Most successful team:\",\n",
        "    winner_count.idxmax()\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"Number of titles:\",\n",
        "    winner_count.max()\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"Most runner-up finishes:\",\n",
        "    runner_up_count.idxmax()\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"Number of runner-up finishes:\",\n",
        "    runner_up_count.max()\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"India's titles:\",\n",
        "    india_wins\n",
        ")\n",
        "\n",
        "print(\n",
        "    \"India's runner-up finishes:\",\n",
        "    india_runnerups\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wD8ok6rUufD1",
        "outputId": "04d0514f-0185-4b59-aaf1-0e7cee373960"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "========== WORLD CUP SUMMARY ==========\n",
            "Total World Cups: 13\n",
            "Different winning teams: 6\n",
            "Different host entries: 9\n",
            "Most successful team: Australia\n",
            "Number of titles: 6\n",
            "Most runner-up finishes: England\n",
            "Number of runner-up finishes: 3\n",
            "India's titles: 2\n",
            "India's runner-up finishes: 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "final_summary = (\n",
        "    winner_count\n",
        "    .rename(\"World Cup Titles\")\n",
        "    .reset_index()\n",
        ")\n",
        "\n",
        "final_summary.columns = [\"Team\", \"World Cup Titles\"]\n",
        "\n",
        "final_summary"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 237
        },
        "id": "2ZS1IfpcunVQ",
        "outputId": "2c2af784-18a1-4b40-977c-bc7d56aa89d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          Team  World Cup Titles\n",
              "0    Australia                 6\n",
              "1  West Indies                 2\n",
              "2        India                 2\n",
              "3     Pakistan                 1\n",
              "4    Sri Lanka                 1\n",
              "5      England                 1"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-6b8ac965-1255-488b-8eba-e3d25f59f051\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Team</th>\n",
              "      <th>World Cup Titles</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Australia</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>West Indies</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>India</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Pakistan</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Sri Lanka</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>England</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6b8ac965-1255-488b-8eba-e3d25f59f051')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-6b8ac965-1255-488b-8eba-e3d25f59f051 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-6b8ac965-1255-488b-8eba-e3d25f59f051');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "  <div id=\"id_7b8aeafc-80bb-4c3d-b838-ae9ca809038a\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('final_summary')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_7b8aeafc-80bb-4c3d-b838-ae9ca809038a button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('final_summary');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "final_summary",
              "summary": "{\n  \"name\": \"final_summary\",\n  \"rows\": 6,\n  \"fields\": [\n    {\n      \"column\": \"Team\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Australia\",\n          \"West Indies\",\n          \"England\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"World Cup Titles\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1,\n        \"min\": 1,\n        \"max\": 6,\n        \"num_unique_values\": 3,\n        \"samples\": [\n          6,\n          2,\n          1\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(12, 7))\n",
        "\n",
        "host_count.sort_values().plot(kind=\"barh\")\n",
        "\n",
        "plt.title(\"ICC Men's Cricket World Cup Hosts\")\n",
        "plt.xlabel(\"Number of Tournaments\")\n",
        "plt.ylabel(\"Host\")\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 707
        },
        "id": "zsnOI-YeutPi",
        "outputId": "89935ae4-aaa6-45c1-e5e9-99b45eeb42a5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1200x700 with 1 Axes>"
            ],
            "image/png": "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wgvy9PTUhQsXdPHiRUuIlJCQkGO8ypUrq3Llyho9erT69u2rJUuWqHv37rK3t7cs3p2fuLg4VahQwWrB8JMnTxb4ms6ePasjR47o448/tsxu2rlzZ559SpQoIScnJ23fvt0yM2fUqFG6cOGC+vbtqy5duqhRo0YFruG1115TpUqVFBUVZbW/Xr16+uKLL+Tr65vrAuo315WaM2eOJYAKDg7WzJkzde7cOb388st5nnvhwoWWRwLLlSt3yzb16tXTkSNH5O/vf8vj+/btU3Z2tmbPni0bmxuTCvN7fDI2NlahoaGWEDIjI6PQa3NVq1ZNn376qa5cuWIJ027OVgMAAAAA4EHB43u68ba3c+fOadCgQapZs6bV1rNnT8tMn8cee0zOzs569dVXlZSUpBUrVli9oe/y5csaMWKEYmJidPLkScXGxmrv3r2qVq2apBtvXcvIyNC2bdt05syZXB8Bk6SAgAClpKQoKipKSUlJmjdvntatW1fgaypRooQeeeQRLVy4UMePH9d3332nMWPG5NnHwcFBI0eOVEREhN577z0dO3ZMO3bsUEJCglxcXLRjxw7LYtwFUbp0aY0ZM0bz5s2z2j98+HD99ddf6tu3r/bu3aukpCRt3rxZAwcOtIR2JUqUUGBgoJYvX25Z0LxFixb68ccfdfTo0TxnSsXGxurFF1/Ua6+9Jj8/P/3+++9WW1pamqQbodmyZcsUERGhn3/+WYmJiYqKitKkSZMkSf7+/rp27Zree+89/frrr/r000+1YMGCPK85ICBAa9euVUJCgg4cOKB+/foVegZUv379ZDKZNHjwYB0+fFhff/21Zs2aVagxAAAAAAC43xFK6caje61bt5aHh0eOYz179lR8fLwOHjyokiVL6rPPPtPXX3+tWrVq6fPPP1d4eLilra2trc6ePatnnnlGlStXVu/evdW+fXtFRERIkpo0aaIXXnhBffr0kaenp956661ca+rSpYtGjx6tESNGqE6dOoqLi7O8la8gbGxsFBUVpX379qlmzZoaPXq03n777Xz7TZs2TXPmzNHChQsVGBiofv36ycfHR8nJyWrUqJE6duyoM2fOFLiOsLAwqwXdJcnb21uxsbHKysrSE088oVq1amnUqFEqXry4ZUaSdGNdqaysLEsoVbJkSVWvXl1eXl6qUqVKruf85JNPdPXqVU2aNEllypTJ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9+7dVatWLXl5eSk5OblQ561WrZoOHjxo9da7vy82fitly5aVJG3fvt2yb86cOerUqZP69eunIUOGWNrkJiQkRDExMYqJiVFwcLBlf4sWLfTNN99oz549lkf3fvnlF509e1YzZ85U8+bNVbVq1XwXOa9Xr54OHz4sf3//HJu9vb0kyc7OTq1bt9Zbb72lgwcPKjk5Wd99912e4wIAAAAA8G9AKPUQyczM1O+//261nTlzpsD9hwwZol9++UXjxo3T0aNHtWrVKkVGRkq6MbPpVgICArR27VolJCTowIED6tevX6FnQPXr108mk0mDBw/W4cOH9fXXX2vWrFl59vHx8dGTTz6p4cOHa9myZUpKStK2bduUlJQkFxcXbdiwId/QKCQkRDt37lRCQoJlppQkBQUF6aOPPtLVq1ctodTNmU3vvfeefv31V23YsEFTp07Nc/xx48YpLi5OI0aMUEJCgo4dO6b//ve/loXOv/rqK82bN08JCQk6efKkli1bpuzsbFWpUqUgtw0AAAAAgPsaodRDZNOmTSpTpozV1qxZswL3r1ixotasWaO1a9cqMDBQH374oeXte7k9NvbOO++oRIkSatKkiTp37qy2bduqXr16harb1dVVX375pQ4dOqS6detq4sSJevPNN/Ptt3TpUo0ZM0bTpk1TjRo1NGTIEAUFBenkyZPy8PBQly5ddPny5Vz7h4SE6PLly/L391fp0qUt+4OCgnThwgVVqVJFZcqUkSR5enoqMjJSq1evVvXq1TVz5sx8g7PAwEB9//33Onr0qJo3b666devqtddek7e3tySpePHiWrt2rVq2bKlq1appwYIF+vzzz1WjRo2C3DYAAAAAAO5rJrPZbC7qIvDvNW3aNC1YsECnTp0q6lLwD+np6TfewjdqlWwcbr04OoC7L3lmx6IuAQAAAChSN/8eTUtLk7u7e67tWOgchTJ//nw1bNhQjzzyiGJjY/X2229bHjcDAAAAAAAoKEIpFMqxY8f0xhtv6K+//lL58uX18ssva8KECUVdFgAAAAAA+JchlEKhzJkzR3PmzCnqMgAAAAAAwL8cC50DAAAAAADAcIRSAAAAAAAAMByhFAAAAAAAAAxHKAUAAAAAAADDEUoBAAAAAADAcIRSAAAAAAAAMByhFAAAAAAAAAxnV9QFALi3fopoK3d396IuAwAAAAAAK8yU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JOacJ4mNjVVMTEyp+VSW2jTvKEoBNdD58+dVXFyswMBAp/bAwMByn3ly5syZKvXHvVGd3LVt21Zvv/22PvzwQ7377rsqKSlRVFSUTp065YqQUU3lzblLly7p6tWrbooKldG8eXO9+eabev/99/X+++8rKChIvXv31t69e90d2n2tpKREcXFxevTRR9WhQ4dy+3G98zyVzR3XO89x4MABNWjQQD4+Pho/frxSUlIUHh5eZl/mnGepSu6Yc54jOTlZe/fu1bx58yrVvzbNuzruDgAAULHIyEin/+GKiopSu3bttHz5cs2ZM8eNkQG1U9u2bdW2bVvH66ioKOXn52vhwoV655133BjZ/S02NlYHDx7Ujh073B0KqqiyueN65znatm0ru92ur7/+Wv/61780cuRIZWRklFvcgOeoSu6Yc57h5MmTmjx5sjZt2nRfPmieohRQAz344IPy9vbW2bNnndrPnj2rZs2alXlMs2bNqtQf90Z1cnerunXrqkuXLvrss8/uRYi4S8qbczabTfXq1XNTVKiuHj16UAxxo0mTJik1NVXbtm1Ty5YtK+zL9c6zVCV3t+J65z5Wq1Vt2rSRJHXr1k3Z2dlavHixli9fXqovc86zVCV3t2LOuUdOTo7OnTunrl27OtqKi4u1bds2/fnPf9a3334rb29vp2Nq07zj9j2gBrJarerWrZs2b97saCspKdHmzZvLvWc8MjLSqb8kbdq0qcJ7zHH3VSd3tyouLtaBAwfUvHnzexUm7gLmXO1it9uZc25gjNGkSZOUkpKiLVu26Ic//OFtj2HueYbq5O5WXO88R0lJib799tsy9zHnPFtFubsVc849+vbtqwMHDshutzu27t27a/jw4bLb7aUKUlItm3fuftI6gOpJTk42Pj4+ZsWKFebw4cPmN7/5jWnUqJE5c+aMMcaYESNGmGnTpjn6Z2Zmmjp16pj58+ebI0eOmPj4eFO3bl1z4MABd53CfauquZs1a5bZuHGjyc/PNzk5OWbYsGHG19fXHDp0yF2ncF+6fPmyyc3NNbm5uUaSWbBggcnNzTWFhYXGGGOmTZtmRowY4ej/+eefm/r165upU6eaI0eOmGXLlhlvb2+zYcMGd53CfauquVu4cKFZs2aNOXbsmDlw4ICZPHmy8fLyMh9//LG7TuG+NWHCBOPv72/S09PN6dOnHds333zj6MP1zjNVJ3dc7zzDtGnTTEZGhjl+/LjZv3+/mTZtmrFYLOajjz4yxjDnPFlVc8ec81y3/va92jzvKEoBNdjSpUtNq1atjNVqNT169DC7du1y7OvVq5cZOXKkU//33nvPhIWFGavVatq3b2/WrVvn4ohxQ1VyFxcX5+gbGBhoBg4caPbu3euGqO9vW7duNZJKbTdyNXLkSNOrV69Sx0RERBir1Woeeughk5SU5PK4UfXcJSYmmtatWxtfX1/TuHFj07t3b7Nlyxb3BH+fKytvkpzmEtc7z1Sd3HG98wxjxowxwcHBxmq1moCAANO3b19HUcMY5pwnq2rumHOe69aiVG2edxZjjHHduiwAAAAAAACAZ0oBAAAAAADADShKAQAAAAAAwOUoSgEAAAAAAMDlKEoBAAAAAADA5ShKAQAAAAAAwOUoSgEAAAAAAMDlKEoBAAAAAADA5ShKAQAAAAAAwOUoSgEAAOCuKSgokMVikd1ud3coDkePHtUjjzwiX19fRUREuDscAADwPxSlAAAAapFRo0bJYrEoISHBqX3NmjWyWCxuisq94uPj5efnp7y8PG3evLnUfovFUuE2c+ZM1wddA/Tu3VtxcXHuDgMAUINRlAIAAKhlfH19lZiYqIsXL7o7lLvmu+++q/ax+fn5+vGPf6zg4GA1adKk1P7Tp087tkWLFslmszm1vfjii3cSeinFxcUqKSm5q2MCAFATUZQCAACoZfr166dmzZpp3rx55faZOXNmqVvZFi1apJCQEMfrUaNGaciQIZo7d64CAwPVqFEjzZ49W9evX9fUqVPVuHFjtWzZUklJSaXGP3r0qKKiouTr66sOHTooIyPDaf/Bgwc1YMAANWjQQIGBgRoxYoTOnz/v2N+7d29NmjRJcXFxevDBBxUdHV3meZSUlGj27Nlq2bKlfHx8FBERoQ0bNjj2WywW5eTkaPbs2eWuemrWrJlj8/f3l8Vicbxu2rSpFixYUO746enpslgs+uqrrxxtdrtdFotFBQUFkqQVK1aoUaNGWrt2rcLDw+Xj46MTJ04oJCREc+fO1ZgxY9SwYUO1atVKf/3rX51i+8Mf/qCwsDDVr19fDz30kGbMmKFr16459t/I49tvv61WrVqpQYMGmjhxooqLi/Xqq686zuGVV15xGverr77S2LFjFRAQIJvNpj59+mjfvn2lxn3nnXcUEhIif39/DRs2TJcvX5b0/XcjIyNDixcvdqwoKygo0MWLFzV8+HAFBASoXr16Cg0NLfP7AQCARFEKAACg1vH29tbcuXO1dOlSnTp16o7G2rJli7744gtt27ZNCxYsUHx8vJ544gk98MAD2r17t8aPH69x48aVep+pU6dqypQpys3NVWRkpAYNGqQLFy5I+r4g0qdPH3Xp0kV79uzRhg0bdPbsWQ0dOtRpjH/84x+yWq3KzMzUm2++WWZ8ixcv1uuvv6758+dr//79io6O1uDBg3Xs2DFJ36+Cat++vaZMmVKtVU+3G7+yvvnmGyUmJuqtt97SoUOH1LRpU0nS66+/ru7duys3N1cTJ07UhAkTlJeX5ziuYcOGWrFihQ4fPqzFixfrb3/7mxYuXOg0dn5+vtLS0rRhwwatXLlSf//73xUTE6NTp04pIyNDiYmJ+uMf/6jdu3c7jnn66ad17tw5paWlKScnR127dlXfvn315ZdfOo27Zs0apaamKjU1VRkZGY7bQhcvXqzIyEj9+te/dqwoCwoK0owZM3T48GGlpaXpyJEjeuONN/Tggw9W6bMCANxHDAAAAGqNkSNHmieffNIYY8wjjzxixowZY4wxJiUlxdz8T7/4+HjTuXNnp2MXLlxogoODncYKDg42xcXFjra2bduan/zkJ47X169fN35+fmblypXGGGOOHz9uJJmEhARHn2vXrpmWLVuaxMREY4wxc+bMMf3793d675MnTxpJJi8vzxhjTK9evUyXLl1ue74tWrQwr7zyilPbww8/bCZOnOh43blzZxMfH3/bsYwxJikpyfj7+1d6/K1btxpJ5uLFi479ubm5RpI5fvy4Y0xJxm63O40THBxsnnvuOcfrkpIS07RpU/PGG2+UG99rr71munXr5ngdHx9v6tevby5duuRoi46ONiEhIaXyNm/ePGOMMdu3bzc2m83897//dRq7devWZvny5eWOO3XqVNOzZ0/H6169epnJkyc7jTFo0CAzevTocuMHAOBmddxZEAMAAMC9k5iYqD59+tzRM5Hat28vL6//X1wfGBioDh06OF57e3urSZMmOnfunNNxkZGRjj/XqVNH3bt315EjRyRJ+/bt09atW9WgQYNS75efn6+wsDBJUrdu3SqM7dKlS/riiy/06KOPOrU/+uijTreiVdfdHN9qtapTp06l2m9uu3Hb4M2f5apVq7RkyRLl5+erqKhI169fl81mcxojJCREDRs2dLwODAyUt7d3qbzdGHffvn0qKioq9Xytq1evKj8/v9xxmzdvXirPt5owYYKeeuop7d27V/3799eQIUMUFRVV4TEAgPsXRSkAAIBa6rHHHlN0dLReeukljRo1ymmfl5eXjDFObTc/q+iGunXrOr22WCxltlXlwd1FRUUaNGiQEhMTS+1r3ry5489+fn6VHtNdbhR+bv4sy/oc69WrV+ZvP6zos9y5c6eGDx+uWbNmKTo6Wv7+/kpOTtbrr79+2zEqGreoqEjNmzdXenp6qXgaNWpUqdjKM2DAABUWFmr9+vXatGmT+vbtq9jYWM2fP7/C4wAA9yeeKQUAAFCLJSQk6N///rd27tzp1B4QEKAzZ844FVPsdvtde99du3Y5/nz9+nXl5OSoXbt2kqSuXbvq0KFDCgkJUZs2bZy2qhSibDabWrRooczMTKf2zMxMhYeH3/E5VGb8gIAASd8/u+qGu/U5ZmVlKTg4WNOnT1f37t0VGhqqwsLCOx63a9euOnPmjOrUqVPq86/K85+sVquKi4tLtQcEBGjkyJF69913tWjRolIPbwcA4AaKUgAAALVYx44dNXz4cC1ZssSpvXfv3vrPf/6jV199Vfn5+Vq2bJnS0tLu2vsuW7ZMKSkpOnr0qGJjY3Xx4kWNGTNGkhQbG6svv/xSzz77rLKzs5Wfn6+NGzdq9OjRZRY5KjJ16lQlJiZq1apVysvL07Rp02S32zV58uS7ch63G79NmzYKCgrSzJkzdezYMa1bt67USqbqCg0N1YkTJ5ScnKz8/HwtWbJEKSkpdzxuv379FBkZqSFDhuijjz5SQUGBsrKyNH36dO3Zs6fS44SEhGj37t0qKCjQ+fPnVVJSoj/96U/68MMP9dlnn+nQoUNKTU11FCMBALgVRSkAAIBabvbs2aVuu2rXrp3+8pe/aNmyZercubM++eSTO3r21K0SEhKUkJCgzp07a8eOHVq7dq1jFc6N1UfFxcXq37+/OnbsqLi4ODVq1MjpOUiV8bvf/U4vvPCCpkyZoo4dO2rDhg1au3atQkND78p53G78unXrauXKlTp69Kg6deqkxMREvfzyy3flvQcPHqznn39ekyZNUkREhLKysjRjxow7HtdisWj9+vV67LHHNHr0aIWFhWnYsGEqLCxUYGBgpcd58cUX5e3trfDwcAUEBOjEiROyWq166aWX1KlTJz322GPy9vZWcnLyHccMAKidLObWhwkAAAAAAAAA9xgrpQAAAAAAAOByFKUAAAAAAADgchSlAAAAAAAA4HIUpQAAAAAAAOByFKUAAAAAAADgchSlAAAAAAAA4HIUpQAAAAAAAOByFKUAAAAAAADgchSlAAAAAAAA4HIUpQAAAAAAAOByFKUAAAAAAADgchSlAAAAAAAA4HL/B3aLLr+m2NfgAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "winner_col = next(\n",
        "    col for col in world_cup_df.columns\n",
        "    if \"winner\" in col.lower()\n",
        ")\n",
        "\n",
        "runner_up_col = next(\n",
        "    col for col in world_cup_df.columns\n",
        "    if \"runner\" in col.lower()\n",
        ")\n",
        "\n",
        "print(\"Winner column:\", winner_col)\n",
        "print(\"Runner-up column:\", runner_up_col)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EzvhjeVnvGxl",
        "outputId": "34c168dd-a64e-45ca-888a-04ccbe42082c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Winner column: Winner\n",
            "Runner-up column: Runner_Up\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Conclusion\n",
        "\n",
        "This project analyzed historical ICC Men's Cricket World Cup data using Python, Pandas, and Matplotlib.\n",
        "\n",
        "The analysis examined World Cup hosts, winning teams, runner-up finishes, and India's performance. Frequency analysis was used to identify patterns in tournament success, while visualizations were created to make the results easier to understand.\n",
        "\n",
        "The project demonstrates how Python can be used to clean, analyze, summarize, and visualize sports data. The results provide an overview of World Cup history and show how tournament success and hosting have changed across different editions."
      ],
      "metadata": {
        "id": "cXegoPLyu3ER"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Key Findings\n",
        "\n",
        "1. The dataset contains historical ICC Men's Cricket World Cup information.\n",
        "2. World Cup titles are distributed among several international teams.\n",
        "3. Runner-up analysis identifies teams that have frequently reached the final.\n",
        "4. England has 3 runner-up finishes in the analyzed dataset.\n",
        "5. The host analysis shows that World Cup hosting has been shared among different countries and country combinations.\n",
        "6. India's World Cup title and runner-up records can be examined separately.\n",
        "7. Pandas was used for data analysis and frequency calculations.\n",
        "8. Matplotlib was used to create the project visualizations."
      ],
      "metadata": {
        "id": "SdWgEFIKu8Gm"
      }
    }
  ]
}
