#include <iostream>
#include <fstream>

#include <openMVG/matching/indMatch.hpp>
#include <openMVG/matching/indMatch_utils.hpp>

int main(int argc, char** argv)
{
    std::string fileIn, fileOut;
    if (argc > 2)
    {
        fileIn = std::string(argv[1]);
        fileOut = std::string(argv[2]);
    }
    else
        return 0;

    openMVG::matching::PairWiseMatches matches;
    openMVG::matching::Load(matches, fileIn);

    auto pairs = openMVG::matching::getPairs(matches);
    std::vector<std::pair<std::size_t, std::size_t>> sortedPairs;
    sortedPairs.reserve(pairs.size());

    for (const auto& pair : pairs)
        sortedPairs.push_back(pair);

    std::sort(std::begin(sortedPairs), std::end(sortedPairs));

    std::ofstream csvFile;
    csvFile.open(fileOut);
    for (const auto& pair : pairs)
    {
        auto i = pair.first;
        auto j = pair.second;

        csvFile
            << i << ","
            << j << ","
            << matches.at(pair).size() << std::endl;
    }
    csvFile.close();

    return 0;
}
